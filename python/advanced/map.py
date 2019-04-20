import gevent
from collections import Mapping, MutableMapping

if __name__ == "__main__":
    a = {}
    print(isinstance(a, Mapping))
    b = ()
    # print(b.__hash__())
    a.setdefault('a', 100)
    print(a)
    a.setdefault('a', 1200)
    print(a)
