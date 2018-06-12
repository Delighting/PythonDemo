#!/usr/bin/env python3

def test(a, b = 99):
  return a >b

print(test(1))

print(test(6, 1))

print('='*20)

def error(a, data = []):
  data.append(a)
  return data

print(error(1))
print(error(2))
print(error(3))

print('='*20)

def right(a, data = None):
  if(data is None):
    data = []
  data.append(a)
  return data

print(right(1))
print(right(2))
print(right(3))