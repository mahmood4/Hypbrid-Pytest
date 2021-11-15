import requests
from bs4 import BeautifulSoup
from bs4 import *
import pandas as pd
import time

url = 'https://dvago.pk/collections/cardio-vascular-system?page=1&grid_list=grid-view'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find_all('div', class_='productitem')
# print(content)
for property in content:
    names = property.find('div', class_='productitem--info')
    name = names.find('h2', class_='productitem--title').text.strip()
    brand = property.find('h3', class_='productitem--vendor').text.strip()

    print(name, brand)