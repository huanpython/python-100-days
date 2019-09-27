# -*- coding: utf-8 -*-
# 开发时间   ：2019/9/27 0027  下午 3:58 
# 文件名称   ：fileimprotant.PY
# 开发工具   ：PyCharm


import shutil
import os

path = 'C:/Users/Administrator/Desktop/201909'

files = os.listdir(path)

for f in files:
    # f.png
    #./png
    print(f.split('-')[-1].split('.')[-2])
    folder_name = f.split('-')[-1].split('.')[-2]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(path+'/'+f,folder_name)
    else:
        shutil.move(path+'/'+f,folder_name)