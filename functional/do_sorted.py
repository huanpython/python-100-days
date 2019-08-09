# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:52 
# 文件名称   ：do_sorted.PY
# 开发工具   ：PyCharm


from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))

