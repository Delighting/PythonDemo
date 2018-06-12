#!/usr/bin/env python3

basket = {'aa', 'bb', 'cc'}

print(basket)

print('bb' in basket)
print('dd' in basket)

a=set('abcdadb')
b=set('ddaabb')

print('a={},b={}'.format(a,b))

print(a - b)

print(a | b)

print(a & b)

print(a ^ b)

print(a.pop())

a.add('g')

print(a)