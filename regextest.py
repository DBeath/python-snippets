import re

regex = re.compile('(.*)(by|By|BY)\s')
suffixRegex = re.compile('\s((in)|(for))(.*)')

text = 'By Joe Blogs for Blah blah'
text2 = 'Zoe Williams in Liverpool'

text = regex.sub('', text)
text = suffixRegex.sub('', text)
print('|{0}|'.format(text.strip()))

print('|{0}|'.format(suffixRegex.sub('', text2).strip()))
