from nameparser import HumanName
from pprint import pprint

n1 = HumanName('Nicholas Lee <MetDesk>')
pprint(n1)

n2 = HumanName('Neelima Choahan, with Adam Cooper and Nick Miller')
pprint(n2)

n3 = HumanName('Maria L La Ganga')
pprint(n3)

n4 = HumanName('Tim')
pprint(n4)
