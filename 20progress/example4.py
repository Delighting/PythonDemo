import sys
import time

n = 10
for i in range(10):
  time.sleep(0.3)
  sys.stdout.write('\r')
  sys.stdout.write(str(i)*(n-1))
  sys.stdout.flush()
  n -= 1
print()
