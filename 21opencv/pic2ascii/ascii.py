from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file') # 输入文件
parser.add_argument('-o', '--output') #结果输出到文件
parser.add_argument('--w', type=int, default=80) # 输出宽度
parser.add_argument('--h', type=int, default=80) #输出高度

args = parser.parse_args()

IMG = args.file
OUT = args.output
WIDTH = args.w
HEIGHT = args.h

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
  """
  rgb转化成ascii
  """
  if alpha == 0:
    return ' '

  charlen = len(ascii_char)
  gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
  unit = (256.0 + 1)/charlen
  return ascii_char[int(gray/unit)]

if __name__ == '__main__':
  im = Image.open(IMG)
  im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

  txt= ''

  for i in range(HEIGHT):
    for j in range(WIDTH):
      txt += get_char(*im.getpixel((j,i)))
    txt += '\n'

  print(txt)

  #字符画输出到文件
  if OUT: 
    with open(OUT,'w') as f: 
      f.write(txt) 
  else: 
    with open("output.txt",'w') as f: 
      f.write(txt)
