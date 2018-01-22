import re

emailRegex = re.compile('[\w.-]+@[\w.-]+')
emailWithBracketsRegex = re.compile('[\{\(\[\<]?[\w.-]+@[\w.-]+[\}\]\)\>]?')

name = "John Doe {john@doe.com}"

out = emailWithBracketsRegex.search(name)

print(out.group(0))
