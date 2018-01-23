from bs4 import BeautifulSoup

html = '<div><p>Testing</p></div><div class="feedflare"><p>Feedflare</p></div>'

soup = BeautifulSoup(html, 'html.parser')

print(type(soup))

print(isinstance(soup, BeautifulSoup))

for div in soup.findAll('div', 'feedflare'):
    div.decompose()

print(str(soup))
