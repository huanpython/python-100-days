# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:25 
# 文件名称   ：algorithm_for.PY
# 开发工具   ：PyCharm

# 打印九九乘法表

for i in range(1,10):
    # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()

