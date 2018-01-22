from bs4 import BeautifulSoup
import requests

urls = ['https://ticketfrog.ch/',
        'https://ticketfrog.ch/de',
        'https://ticketfrog.ch/de/veranstalter/kostenlos.html',
        'https://ticketfrog.ch/de/veranstalter',
        'https://ticketfrog.ch/de/help.html']

links = []
hrefs = []

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links.extend(soup.find_all('a'))

linkSet = set(links)

for a in linkSet:
    href = a.get("href", None)
    if href:
        hrefs.append(a)
        print(a.get('href'))
        print()

for a in hrefs:
    if 'preis' in a.get('href', ''):
        print('FOUND LINK')
        print(a)

    if 'kostenlos' in a.get('href', ''):
        print('FOUND KOSTENLOS')
        print(a)
