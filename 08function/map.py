#!/usr/bin/env python3

lst = [1, 2, 3, 4]

def square(num):
  '返回给定数字的平方'
  return num * num

print(square.__doc__)
print(list(map(square,lst)))