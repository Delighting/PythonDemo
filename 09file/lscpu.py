#!/usr/bin/env python3

cpu = open('/proc/cpuinfo','r')

for line in cpu:
  print(line)
cpu.close()