#!/usr/bin/env python3

file = open('./String.txt')

news=''

for s in file.read():
  if s.isdigit():
    news += s

print(news)
