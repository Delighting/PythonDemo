"""
learn conter
"""

from collections import Counter
import re

path = '/usr/lib/python3.5/LICENSE.txt'

words = re.findall('\w+',open(path).read().lower())

c = Counter(words)

print(c.most_common(10))

c2 = Counter(a=2,b=0,c=4,d=-1)

print(list(c2.elements()))