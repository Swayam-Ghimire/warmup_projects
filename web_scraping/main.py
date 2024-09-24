import requests
from bs4 import BeautifulSoup as bs


github = input('Enter the github usename: ')
url = 'https://github.com/'+github
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profileImg = soup.find('img', {'width':260})['src']
print(profileImg)