from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


src = requests.get("https://mangapark.net/")
soup = BeautifulSoup(src.content, 'html.parser')
parent = soup.find('article')


dict = []
# file = open('fiel.jpg', 'wb')
for i in parent.find_all('img'):
	dict.append('https:'+i.get('src'))


for i in range(len(dict)):
	r = requests.get(dict[i])
	with open('image{}.jpg'.format(dict[i][42:50]), 'wb') as f:
		f.write(r.content)


