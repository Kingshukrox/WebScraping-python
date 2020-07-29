import requests
import re
from bs4 import BeautifulSoup
url='https://www.flipkart.com/kingston-a400-120-gb-laptop-desktop-internal-solid-state-drive-sa400s37-120g/product-reviews/itmeswy69utguggz?pid=IHDFF8WMGEZQ8EJQ'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
data=soup.find_all("div",{"class":"qwjRop"})
for item in data:
    review=item.find_all("div",{"class":""})[0]
    print(review.text.replace("READ MORE",""))
