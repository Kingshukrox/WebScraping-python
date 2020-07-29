import requests
from bs4 import BeautifulSoup

# EXAMPLE LINK https://github.com/Kingshukrox?tab=repositories
# TAG WHERE NAME OF THE REPO IS STORED(more <a> tag within this) wb-break-all
# ABOUT p-note user-profile-bio mb-3 js-user-profile-bio f4
username = input('Enter the exact username: ')
url = 'https://github.com/' + username + '?tab=repositories'
urlopen = requests.get(url)
if str(urlopen) != '<Response [200]>':
    print('USERNAME NOT FOUND')
    exit()
urlopen = urlopen.text
soup = BeautifulSoup(urlopen, 'html.parser')
about_tag = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
print('------------------ABOUT------------------\n')
try:
    print(about_tag.find('div').text)
except:
    print('No About section found')
repo_class_tag = soup.find_all('h3', class_='wb-break-all')
repo_list = list()
for i in repo_class_tag:
    repo_list.append(i.find('a').text.strip())
print('\n------------------REPOSITORIES (' +
      str(len(repo_list)) + ')--------------------')

if len(repo_list) < 1:
    print('\nNo repositories found')
    exit()

for i in range(len(repo_list)):
    print(i+1, '->', repo_list[i])
