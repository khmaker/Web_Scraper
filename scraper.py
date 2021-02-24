import requests
from bs4 import BeautifulSoup
from string import punctuation
from os import mkdir

base_url = 'https://www.nature.com'
target_url = 'https://www.nature.com/nature/articles'


def get_soup(url):
    r = requests.get(url)
    code = r.status_code
    return BeautifulSoup(r.content, 'html.parser') if code == 200 else None


def select_from_soup(soup, look_for):
    return soup.select(look_for)


def is_type(soup, article_type='News'):
    selection = select_from_soup(soup, 'span[data-test="article.type"]')
    return selection[0].text == article_type if selection else False


def get_article(url):
    soup = get_soup(url)
    article_classes = ['.article__body', '.article-item__body']
    for article_class in article_classes:
        article_body = select_from_soup(soup, article_class)
        if article_body:
            return article_body[0].text.strip()


def get_link_and_title(soup):
    selection = select_from_soup(soup, 'a[data-track-action="view article"]')
    link = selection[0].get('href') if selection else None
    title = selection[0].text if selection else None
    return link, title


def transform(title):
    t = str.maketrans('', '', punctuation)
    title = title.translate(t)

    return title.strip().replace(' ', '_')


def make_file(link, title, directory='.'):
    title = transform(title)
    link = base_url + link
    with open(f'{directory}/{title}.txt', 'wb') as f:
        content = get_article(link)
        if content is not None:
            f.write(content.encode('utf-8'))


def save_articles(page, article_type):
    url = target_url + f'?page={page}'
    articles = get_soup(url).find_all('article')
    directory = f'Page_{page}'
    mkdir(directory)
    for article in articles:
        if is_type(article, article_type):
            article_link, article_title = get_link_and_title(article)
            if article_link and article_title:
                make_file(article_link, article_title, directory)


if __name__ == '__main__':

    page_range = int(input())
    user_article_type = input()
    for page_num in range(page_range):
        save_articles(page_num + 1, user_article_type)
    print('Saved all articles.')
