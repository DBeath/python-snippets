import json
from pprint import pprint

with open('theguardian2.json') as f:
    data = json.load(f)


pprint(data)
