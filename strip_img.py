from bs4 import BeautifulSoup
from pprint import pprint
import time

with open('boingboingentry.html', 'r') as f:
    html = f.read()

totalstart = time.time()
soup = BeautifulSoup(html, 'lxml')


images = soup.find_all("img")
# pprint(images)

for img in images:

    # pprint(vars(img))
    # pprint(img['height'])
    del img['height']
    del img['width']

    del img['width']

    img['style'] = u'max-width:100%;'

# pprint(vars(img))

out = soup.encode('utf-8', formatter=None)
print(out)

with open('boingboingentry_parsed.html', 'w+') as f:
    f.write(out)

totalend = time.time()
print('Total time {0}'.format(totalend - totalstart))
