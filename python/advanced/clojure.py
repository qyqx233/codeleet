import logging
logging.basicConfig(level=logging.DEBUG)
# 定义在模块最外层的是全局变量，模块内部的函数也能访问到
num = 10


def foo():
    print(num)


def fx():
    # nonlocal x
    x = 100

    def fy():
        print(x)
    fy()


def fa():
    count = 0

    logging.debug('before exec inner func: count=%d', count)

    def fb():
        nonlocal count
        count = 2
    fb()
    logging.debug('after exec inner func: count=%d', count)


def counter():
    n = 0

    def fun():
        nonlocal n
        n += 1
        return n
    return fun


class A:
    def __init__(self):
        self.a = 0


def fclass():
    a = A()

    def fun():
        return a
    return fun


def test_foo():
    foo()


def test_counter():
    c1 = counter()
    logging.debug(c1())
    c2 = counter()
    logging.debug(c2())
    logging.debug(c2())
    logging.debug(c1())
    logging.debug(c1.__closure__[0].cell_contents)
