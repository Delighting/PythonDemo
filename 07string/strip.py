#!/usr/bin/env python3

a = ' cc test'
print(a.strip())

b = 'aabbccdd'

print(b.strip('aa'))

print(b.lstrip('aa'))

print(b.rstrip('aa'))

print(b.find('b'))

print(b.find('bb'))

print(b.startswith('aa'))

print(b.endswith('bb'))