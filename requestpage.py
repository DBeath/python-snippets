import requests

url = 'https://www.theatlantic.com'

user_agent = "feedfindertest"
user_agent = None

with requests.Session() as s:
    s.max_redirects = 50
    r = s.get(url,
              headers={
                  "User-Agent": user_agent
              },
              timeout=(5, 20))

print(r)
print(r.history)
