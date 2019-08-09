# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:25 
# 文件名称   ：algorithm_for.PY
# 开发工具   ：PyCharm

# 判断是否是闰年

year =int(input("请输入一个年份："))

if(year%4)==0 and (year%100) !=0 or (year%400) ==0:
    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))

