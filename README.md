# Web Scraper
Study project from [JetBrains Academy](https://hyperskill.org/projects/145)

## About
You will create a function that takes a website address and a number of webpages as input arguments and then goes all over the website saving every news article on the page to a separate .txt file on your computer.

## Description
1. The function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
2. Go back to the https://www.nature.com/nature/articles website and find out how to navigate between the pages with the requests module changing the URL.
3. Create a directory named Page_N (where N is the page number) for each page in the desired category, and put all the articles that are found on the page with the matched type to this directory.
4. Save the articles to separate *.txt files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.

## Example
The program takes two input values from the user and then continues to process the [Nature website](https://www.nature.com/nature/articles) data.
```
> 4
> Nature Briefing
Saved all articles.
```
