#coding=utf-8

import unittest

from factorial import fact

class FacorialTest(unittest.TestCase):
  """
  基本测试类
  """

  def test_fact(self):
    """
    实际测试中以 test_都是测试用例
    """
    res = fact(5)
    self.assertEqual(res, 120)

if __name__ == '__main__':
  unittest.main()