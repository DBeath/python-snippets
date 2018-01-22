import requests

domain = 'www.google.com'

url = 'https://icons.duckduckgo.com/ip2/' + domain

r = requests.get(url)

print(r.status_code)
print(r.text)
