#!/usr/bin/env python3

import sys

print('first args=',sys.argv[0])

for i , x in enumerate(sys.argv):
  print(i,x)