import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import requests


base_url = 'http://books.toscrape.com/'
url_open = requests.get(base_url).text
soup = BeautifulSoup(url_open, 'html.parser')
h3_tags = soup.find_all('h3')
title = list()
for i in h3_tags:
    title.append(i.findChildren('a')[0]['title'])
price = list()
price_color_tag = soup.find_all('p', class_='price_color')
for i in price_color_tag:
    price.append(i.text[1:])
for i in range(len(price)):
    print(price[i], title[i])
