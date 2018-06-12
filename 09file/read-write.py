#!/usr/bin/env python3

file = open('test.txt','w')

file.write('test content.')

file.close()

file2 = open('test.txt','r')

text = file2.read()

print('test.txt content is ',text)

file2.close()

file3 = open('test.txt','a')
file3.write('\nadd test2\n')
file3.close()

file4 = open('test.txt','r')
print('first line=',file4.readline())
print('new content = ', file4.read())
file4.close()

file5 = open('test.txt','r')
for s in file5:
  print(s)

print(file5.readlines())
file5.close()