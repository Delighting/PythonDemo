#!/usr/bin/env python3

import os

print('gid {}, pid {}'.format(os.getgid(),os.getgid()))

print(os.uname())

def view_dir(path = '.'):
  names = os.listdir(path)
  names.sort()
  for name in names:
    print(name, end = ' ')
  print()


view_dir('/home/ll/bin')