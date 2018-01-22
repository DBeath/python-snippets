from werkzeug.urls import url_parse, url_fix
from pprint import pprint
from urllib.parse import urlsplit

# url = 'feeds://boingboing.com/testing/123?query=queryingtest'
url = 'boingboing.net'

parsed = url_parse(url, 'http')

pprint(parsed)

print()

replaced = parsed.replace(scheme='https')
pprint(replaced)
print(replaced.to_url())

print()

parsed2 = urlsplit(url)

pprint(parsed2)


url = 'boingboing.net  '
fixed = url_fix(url)

pprint(fixed)
