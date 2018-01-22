import re
from pprint import pprint

# comment_pattern = '\/comment(?:s)?(?:\/)?'
# comment_regex = re.compile(comment_pattern)

# url = 'http://boingboing.net/comments/feed'
# result = comment_regex.search(url)
# if result:
#     print(result.string)

# r = comment_regex.sub('/', url)
# print(r)

bracketNameRegex = re.compile('(?: *\w+ *)* *([\{\(\[\<]+(?: *\w+ *)*[\}\)\]\>]+)+ *(?: *\w+ *)*')

name = 'Mark hello test blash editor hello'

result = bracketNameRegex.search(name)
print(result)
