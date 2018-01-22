import re
from pprint import pprint

stripChars = '(\( *(\w+)* *\))'

# stripCharRegexPattern = '|'.join(map(re.escape, stripChars))
# pprint(stripCharRegexPattern)
stripCharRegex = re.compile(stripChars)


name = 'Nicholas Lee (MetDesk)'

stripped = stripCharRegex.sub('', name)

pprint(stripped)
