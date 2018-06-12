#!/usr/bin/env python3

class Account(object):

  def __init__(self,rate):
    self.__amt = 0
    self.rate = rate

  @property
  def amount(self):
    """账户余额 美元"""
    return self.__amt

  @property
  def cny(self):
    """账户余额 人民币"""
    return self.__amt* self.rate

  @amount.setter
  def amount(self, value):
    if value <0:
      print('value can not be negetive')
      return
    self.__amt = value

account = Account(7)

account.amount = -100
print(account.amount)

account.amount = 20

print(account.cny)
