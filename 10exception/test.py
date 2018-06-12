#!/usr/bin/env python3

import sys

def Hours(mini):
  minis = int(mini)
  if minis < 0:
    raise ValueError('num is a negtive')
  else:
    
    h, m = divmod(minis, 60)

    hours = int(minis / 60)
    minis = minis % 60

    print('{} H, {} M'.format(hours, minis))
    print('divmod {} H, {} M'.format(h, m))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    try:
      Hours(sys.argv[1])
    except ValueError:
      print('ValueError: can not be negtive num')
  else:
    try:
      Hours(int(input('请输入分钟数：')))
    except ValueError:
      print('ValueError: can not be negtive num')
  exit(0)
