from bs4 import BeautifulSoup
import requests


src = requests.get("https://mangapark.net/")
soup = BeautifulSoup(src.content, 'html.parser')
parent = soup.find('article')


dict = []
for link in parent.find_all('img'):
	dict.append('https:'+link.get('src'))


for i in range(len(dict)):
	r = requests.get(dict[i])
	with open('image{}.jpg'.format(dict[i][42:50]), 'wb') as f:
		f.write(r.content)


