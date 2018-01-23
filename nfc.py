import unicodedata

text = "\ȯk-ˈtȯr-ē-əl\  : of or relating to an author."
output = unicodedata.normalize('NFC', text)

print(output)
