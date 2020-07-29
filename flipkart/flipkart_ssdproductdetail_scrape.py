import requests
import re
import json
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/kingston-a400-120-gb-laptop-desktop-internal-solid-state-drive-sa400s37-120g/p/itmeswy69utguggz?pid=IHDFF8WMGEZQ8EJQ&lid=LSTIHDFF8WMGEZQ8EJQVLGADG&marketplace=FLIPKART&srno=s_1_1&otracker=search&fm=SEARCH&iid=45cb83a8-b6d3-4a86-85b6-eeeec8773be5.IHDFF8WMGEZQ8EJQ.SEARCH&ppt=CLP&ppn=CLP%3Amens-watches-store&ssid=m5urqa3g0w0000001545143218972&qH=d4576b3b305e1df6'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
rev = []
data = soup.find_all("div", {"class": "qwjRop"})
for item in data:
    review = item.find_all("div", {"class": ""})[0]
    print(review.text.replace("READ MORE", ""))
    rev.append(review.text.replace("READ MORE", ""))
with open("a.txt", 'w') as outfile:
    json.dump(rev, outfile)
