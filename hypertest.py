from hyper import HTTPConnection
from hyper.contrib import HTTP20Adapter
import requests
import time

url = 'https://davidbeath.com'

start = time.perf_counter()
conn = HTTPConnection('davidbeath.com')
conn.request('GET', '/')
resp = conn.get_response()

text = resp.read()
# print(resp.read())
end = time.perf_counter()

start2 = time.perf_counter()
r = requests.get(url)

text2 = r.text
# print(r.text)
end2 = time.perf_counter()

start3 = time.perf_counter()
s = requests.Session()
s.mount(url, HTTP20Adapter())
r3 = s.get(url)
text3 = r3.text
end3 = time.perf_counter()

print('Hyper: GET {0} in {1}ms'
      .format(resp.status,
              int((end - start) * 1000)))

print('Requests: GET {0} in {1}ms'
      .format(r.status_code,
              int((end2 - start2) * 1000)))

print('HyperRequests: GET {0} in {1}ms'
      .format(r3.status_code,
              int((end3 - start3) * 1000)))
