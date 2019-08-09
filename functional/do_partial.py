# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:47 
# 文件名称   ：do_partial.PY
# 开发工具   ：PyCharm


import functools

int2 =functools.partial(int,base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))