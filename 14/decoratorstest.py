def my_decorator(func):
  def wapper(*args, **kwargs):
    print('before fun',args, kwargs)
    result = func(*args, **kwargs)
    print('after fun', result)
    return result
  return wapper

@my_decorator
def add(a, b):
  return a + b

add(1, 2)