#!/usr/bin/env python3

a = [1,2,3,5]

a.append(4)

print(a)

a.insert(3,4)

print(a)

print(a.count(4))

a.remove(5)

print(a)

a.reverse()

print(a)

b = [7,8,9]

a.extend(b)

print(a)

a.sort()

print(a)

del a[0]

del a[-1]

print(a)