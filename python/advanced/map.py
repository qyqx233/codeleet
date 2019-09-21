import gevent
from collections import Mapping, MutableMapping, abc, UserDict, defaultdict


class Hashable():
    def __hash__(self):
        return 1

    # def __eq__(self, v):
    #     return 0


def hashKey():
    a = {}
    a[Hashable()] = 100


hashKey()


class MissingMap(UserDict):
    def __missing__(self, key):
        return 'missing'


def dict_test():
    a = {}
    print(isinstance(a, Mapping))
    # print(b.__hash__())
    a.setdefault('a', 100)
    print(a)
    a.setdefault('a', 1200)
    print(a)
    print(a.__iter__())
    a.update([['a', 2]])
    print(a)


# dict_test()
mm = MissingMap()
print(mm['a'])

dm = defaultdict(int)
print(dm['a'])
