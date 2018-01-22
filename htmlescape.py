# -*- coding: UTF-8 -*-

from bs4.dammit import UnicodeDammit
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

text = 'Nicol&aacute;s Medina Mora'.decode('UTF-8')
text2 = 'Nicolás'.decode('UTF-8')

print(text2)
print(type(text2))
# dammit = UnicodeDammit(text)

# print(dammit.unicode_markup)
# print(dammit.original_encoding)



htmlparser = HTMLParser()

unsub = htmlparser.unescape(text2)
print(unsub)
print(type(unsub))

# out = unsub.encode('UTF-8')
# print(out)

# soup = BeautifulSoup(text2, 'html.parser')
# print(unicode(soup))


print()

print(text)
print(type(text))

unsub2 = htmlparser.unescape(text)
print(unsub2)
print(type(unsub2))
