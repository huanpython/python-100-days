# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:49 
# 文件名称   ：do_reduce.PY
# 开发工具   ：PyCharm

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints =map(lambda ch:CHAR_TO_INT[ch],s)
    return reduce(lambda x,y:x*10+y,ints)


print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

