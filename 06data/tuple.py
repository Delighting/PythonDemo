#!/usr/bin/env python3

a = 1, 2, 3

print(a)

print(a[1])

for x in a:
  print(x, end = ' ')
print()

x, y = divmod(15, 2)

print('x={},y={}'.format(x, y))

b = (1)

print(type(b))

c = (1,)

print(type(c))

print(type(len))