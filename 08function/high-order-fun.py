#!/usr/bin/env python3

def high(fun, value):
  return fun(value)

lts = high(dir, int)

print(lts[-3:])