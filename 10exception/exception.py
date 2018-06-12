#!/usr/bin/env python3

def get_num():
    """
    input float num
    """
    return float(input('请输入浮点数: '))

try:
    print(get_num())
except ValueError:
    print('value error')
