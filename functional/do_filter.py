# -*- coding: utf-8 -*-
# @Time : 2019/8/11 0011 22:37
# @Author : huanfuan
# @FileName: do_filter.py
# @Software: PyCharm


def is_odd(n):
    return n % 2 == 1

L = range(100)

print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
