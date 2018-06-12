#!/usr/bin/env python3

from PIL import Image
import sys,os
from os import path

def create_image(pathstr):
    basename = path.basename(pathstr)
    dic = path.splitext(basename)
    im = Image.open(pathstr)
    im.save(dic[0] + ".jpg", "JPEG")
    print("保存到："+dic[0]+".jpg")

def check(pathstr):
  if path.splitext(pathstr)[1] != ".webp":
    return
  if path.isfile(pathstr):
    return path
  else:
    full_path = os.getcwd() + os.sep + pathstr
    if os.path.isfile(full_path):
      return full_path

def main(filename):
    print("转换： "+filename)
    if check(filename):
      create_image(filename)
    else:
      print("请输入正确的文件名")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
      print("请指定文件")