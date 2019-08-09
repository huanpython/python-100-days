# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 3:59 
# 文件名称   ：dict.PY
# 开发工具   ：PyCharm


dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}

print(dict1)                              # 通过 key 值，删除对应的元素
del dict1['twowater']
print(dict1)                              # 删除字典中的所有元素
dict1.clear()
print(dict1)                              # 删除字典
del dict1