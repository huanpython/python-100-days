# -*- coding: utf-8 -*-
# 开发时间   ：2019/8/9 0009  下午 4:56 
# 文件名称   ：prime_numbers.PY
# 开发工具   ：PyCharm

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x % n>0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    main()