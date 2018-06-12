#!/usr/bin/env python3

class MyClass(object):
  
  i = 1000
  data = []

  def __init__(self, ini, idata):
    self.i = ini
    self.data = idata
  
  def f(self):
    return 'a methon'

x = MyClass(1,[1,2])

print(x.i, ' ', x.data)