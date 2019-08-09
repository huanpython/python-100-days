# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:07 
# 文件名称   ：do_if.PY
# 开发工具   ：PyCharm

age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')