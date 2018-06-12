#!/usr/bin/env python3

a = [1,2,'CC',1.07]
print(a)

print(a[:])

print(a[2:])

print(a[2:-1])

print(a[7:2])

b = a + ['cc','dd']

print(b)

b[4] = 0

print(b)

b[1:3] = []

print(b)

b[:]=[]

print(b)

c = ['cc','dd']

print('cc' in b)

print(len(c))

for i in c:
  print(i)

#自定义步长

d = [0,1,2,3,4,5,6,7,8,9]

for i in d[::2]:
  print(i, end=' ')

print()

#range，range(start,end,setp)

print(range(5))

print(list(range(5)))

print(list(range(1,4)))

print(list(range(1,8,2)))
