import requests
from bs4 import BeautifulSoup

headers={
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 12.6; rv:105.0) Gecko/20100101 Firefox/105.0",
  "Accept-Language":"en"
  }

response = requests.get("https://www.amazon.co.uk/Sage-SJE530BSS-Juicer-Brushed-Stainless/dp/B07Q9RC569/ref=sr_1_2_sspa?crid=EGFKBUGN9DZE&keywords=cold+pressed+juicer&qid=1665578592&qu=eyJxc2MiOiI0LjQ4IiwicXNhIjoiMy44NCIsInFzcCI6IjIuMzIifQ%3D%3D&sprefix=cold+pressed+juicer%2Caps%2C71&sr=8-2-spons&psc=1", headers=headers)

item = response.text

soup = BeautifulSoup(item, 'html.parser')
test = soup.find("span", class_="a-price-whole")
print(test.getText())

