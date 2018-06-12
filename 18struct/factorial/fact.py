"myfact module"

def factorial(num):
  """
  返回给定数字的阶乘
  """
  if num >= 0:
    if num == 0:
      return 1
    return num * factorial(num - 1)
  return -1