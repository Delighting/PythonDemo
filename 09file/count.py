#!/usr/bin/env python3

import os
import sys

def parse_file(path):
  """
  分析文本的空格 制表符 行的相关信息

  ：arg path: 文件路径

  ：return 包含空格、制表符、行数的元组
  """
  fd = open(path)

  i = 0
  spaces = 0
  tabs = 0

  for i,line in enumerate(fd):
    spaces+=line.count(' ')
    tabs += line.count('\t')
  
  fd.close()

  return spaces, tabs, i+1

def main(path):
  if(os.path.exists(path)):
    spaces, tabs, lines = parse_file(path)
    print('space {}, tabs {}, lines {}'.format(spaces,tabs,lines))
    return True
  else:
    return False

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    exit(-1)
  exit(0)