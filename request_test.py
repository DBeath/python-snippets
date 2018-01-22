import requests

url = 'http://jsonfeed.com'

r = requests.get(url)

print(r)
print(r.text)
