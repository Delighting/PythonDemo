
import sys 
import os 
import time 
import threading 
import termios 
import tty 
import cv2 
import pyprind

class CharFrame: 
  ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " 
  # 像素映射到字符 
  def pixelToChar(self, luminance):
    return self.ascii_char[int(luminance/256*len(self.ascii_char))] 
  
  # 将普通帧转为 ASCII 字符帧 
  def convert(self, img, limitSize=-1, fill=False, wrap=False): 
    if limitSize != -1 and (img.shape[0] > limitSize[1] or img.shape[1] > limitSize[0]):
      img = cv2.resize(img, limitSize, interpolation=cv2.INTER_AREA) 
    ascii_frame = '' 
    blank = '' 
    if fill: 
      blank += ' '*(limitSize[0]-img.shape[1]) 
    if wrap: 
      blank += '\n' 
    for i in range(img.shape[0]): 
      for j in range(img.shape[1]): 
        ascii_frame += self.pixelToChar(img[i,j]) 
        ascii_frame += blank 
    return ascii_frame

  class I2Char(CharFrame): 
    result = None 
    def __init__(self, path, limitSize=-1, fill=False, wrap=False): 
      self.genCharImage(path, limitSize, fill, wrap) 
      
    def genCharImage(self, path, limitSize=-1, fill=False, wrap=False): 
      img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
      if img is None: 
        return 
      self.result = self.convert(img, limitSize, fill, wrap) 
      
    def show(self, stream = 2): 
      if self.result is None: 
        return 
      if stream == 1 and os.isatty(sys.stdout.fileno()): 
        self.streamOut = sys.stdout.write
        self.streamFlush = sys.stdout.flush 
      elif stream == 2 and os.isatty(sys.stderr.fileno()): 
        self.streamOut = sys.stderr.write 
        self.streamFlush = sys.stderr.flush 
      elif hasattr(stream, 'write'): 
        self.streamOut = stream.write 
        self.streamFlush = stream.flush 
      
      self.streamOut(self.result)
      self.streamFlush()
      self.streamOut('\n')

  class V2Char(CharFrame):
    def __init__(self, path): 
      if path.endswith('txt'): 
        self.load(path) 
      else: 
        self.genCharVideo(path)

    def genCharVideo(self, filepath): 
      self.charVideo = [] 
      cap = cv2.VideoCapture(filepath) 
      self.timeInterval = round(1/cap.get(5), 3) 
      nf = int(cap.get(7)) 
      print('Generate char video, please wait...') 
      # for i in pyprind.prog_bar(range(nf)): 
        # rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY) 
        # frame = self.convert(rawFrame, os.ge
        