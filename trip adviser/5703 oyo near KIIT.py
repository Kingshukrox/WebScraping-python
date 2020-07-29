import requests
from bs4 import BeautifulSoup
url='https://www.tripadvisor.in/Hotel_Review-g297661-d13157534-Reviews-OYO_5703_near_KIIT_University-Bhubaneswar_Khurda_District_Odisha.html'
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
name=soup.find_all("h1",{"id":"HEADING"})[0]
print(name.text)
data=soup.find_all("div",{"class":"no_cpu offer premium chevron hacComplete  avail "})
for item in data:
    price=item.find_all("div",{"class":"price __resizeWatch"})[0]
    print(price.text)