import re

httpRegex = re.compile('http:\/\/')


def coerce_url(url):
    url = url.strip()
    if url.startswith("feed://"):
        return "https://{0}".format(url[7:])
    for proto in ["http://", "https://"]:
        if url.startswith(proto):
            return url
    return "https://{0}".format(url)


def coerce_https(url):
    return httpRegex.sub('https://', url)


url = 'http://boingboing.net'

print(coerce_https(url))
