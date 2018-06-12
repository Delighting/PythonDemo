#!/usr/bin/env python3

def fun(a, b = 2, c=5):
  print('a=', a, ' b=', b,' c=',c)

fun(1,2)

fun(23, c = 10)

fun(a = 1,b=2,c=10)

fun(b=2 ,c=10, a = 1)


def strongKey(*, name = 'username'):
  print(name)

#strongKey('aa') #error

strongKey(name = 'shiyanlou')