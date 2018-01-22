import requests
import pprint

p = requests.get('http://www.radionz.co.nz')

print p.status_code
print p.text

with open('radionz.html', 'w+') as f:
    f.write(p.text.encode('utf-8'))
