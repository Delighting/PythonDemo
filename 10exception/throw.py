#!/usr/bin/env python3


def throw_exce():
    """
    throw exception
    """
    raise ValueError('value error')

try:
  throw_exce()
except ValueError:
  print('has exception')
finally:
  print('finally')
