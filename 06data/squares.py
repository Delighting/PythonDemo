#!/usr/bin/env python3

squares = []

for i in range(10):
  squares.append(i**2)

print(squares)

squares2 = list(map(lambda x:x**2,range(10)))
print(squares2)

#推到式
squares3 = [x**2 for x in range(10)]
print(squares3)

a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]
print(a)

b = []

for x in [1,2,3]:
  for y in [3,1,4]:
    if(x != y):
      b.append((x,y))
print(b)

c = [x+1 for x in [x ** 2 for x in [1,2,3]]]

print(c)
