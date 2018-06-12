#!/usr/bin/env python3

def change():
  a = 90
  print(a)

a = 9

print('before change a = ' , a)
change()
print('after change a = ', a)


def change2():
  global a
  a = 90
  print(a)

a = 9
print('before change a = ', a)
change2()
print('after change a = ', a)