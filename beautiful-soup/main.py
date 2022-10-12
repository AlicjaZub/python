import os
from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text

soup = BeautifulSoup(yc_page, 'html.parser')

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
article_scores = []

for tag in articles:
  articles_content = tag.find("a")
  article_texts.append(articles_content.getText())
  article_links.append(articles_content.get("href"))

score_spans = soup.find_all(name="span", class_="score")
  
article_scores = [int(score.getText().split()[0]) for score in score_spans]
   
articles_content = [[ article_texts[i], article_links[i], article_scores[i]] for i in range(0, len(article_links) - 1)]
# articles_content = [{ "titile": article_texts[i], "link": article_links[i], "score": article_scores[i]} for i in range(0, len(article_links) - 1)]

for content in articles_content:
  # votes = content[2].split()
  # votes = re.findall(r'\d+', content[2])
  # if int(votes[0]) > 100:
  #   print(content[0], content[1], content[2])
  if content[2] > 250:
    print(content[0], content[1])


# with open(f"{os.getcwd()}/beautiful-soup/website.html") as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.prettify())
# # print(soup.li)
# a_tags = soup.find_all(name="a")

# for a in a_tags:
#   print(a.getText())
#   print(a.get("href"))
  
# heading = soup.find(name="h1", id="name")
# test = soup.select_one("ul li")
# print(test)
