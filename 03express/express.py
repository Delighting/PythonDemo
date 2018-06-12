#!/usr/bin/env python

days = int(input('Enter days: '))

month = days//30

day = days%30

print('month = {}, day= {}'.format(month,day))

print('month = {}, day= {}'.format(*divmod(days, 30)))

