from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = 'http://push-pub.appspot.com/feed'

result = requests.get(url).text

soup = BeautifulSoup(result, 'html.parser')

pprint(soup)

hub = soup.find(name='link', rel='hub')

pprint(type(hub))

href = hub.get('href')
pprint(href)
