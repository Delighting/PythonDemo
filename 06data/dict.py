#!/usr/bin/env python3

data = {'aa':'aaa','bb':'bbb'}

print(data)

#add
data['cc'] = 'ccc'
print(data)

print('cc' in data)

del data['bb']
print(data)

a = ('aa', 'bb')
b = ('aaa', 'bbb')

c = dict((a,b))
print(c)

for x,y in c.items():
  print("{},{}".format(x,y))

print('='*20)
data = {}

data.setdefault('names',[]).append('Ruby')

print(data)

print(data.get('name',0))

print('='*20)

#获取数据和索引
for x,y in enumerate([1,2,3]):
  print("{}:{}".format(x,y))


print('='*20)
for x, y in zip(['a',2], [1,3]):
  print("{}:{}".format(x,y))