import hashlib
import os
import requests
import typing
from collections import defaultdict


def lis1(al, bl):
    '''暴力枚举
    '''
    # print(al, bl)
    if len(al) == 0:
        yield bl[1:]
    for i, a in enumerate(al):
        if a < bl[-1]:
            # continue
            ...
        for v in lis1(al[i + 1:], bl + [a]):
            yield v


def foo(al: typing.List, target: int):
    d = defaultdict(int, {al[0]: 1, al[0] * -1: 1})
    for i in range(1, len(al)):
        d1 = defaultdict(int)
        v = al[i]
        for key, val in d.items():
            d1[key + v] += val
            d1[key - (1 * v)] += val
        d = d1


def xoo():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        pass


def md5(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()


# for i in lis1([1, 3, 2], [-1]):
    # print(i)
if __name__ == '__main__':
    # print(defaultdict(int, {'a': 100}))
    # foo([1, 10, 100, 1000, 10000, 100000], 3)
    # print(md5("abcd"))
    print(os.getcwd())
    res = requests.post("http://58.210.114.60/apprequest/memapplication", json={})
    print(res.status_code)
    print(res.content)
    with open("a.txt", 'w', encoding='utf8') as fw:
        fw.write(res.content.decode('utf8'))
