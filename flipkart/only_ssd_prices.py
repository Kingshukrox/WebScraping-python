from bs4 import BeautifulSoup
import requests
url='https://www.flipkart.com/search?q=ssd&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
data=soup.find_all("a",{"class":"_1Vfi6u"})
for item in data:
    price=item.find_all("div",{"class":"_1vC4OE"})[0]
    print(price.text)