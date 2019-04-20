import functools


class adaptee(object):
    def foo(self):
        print('foo in adaptee')

    def bar(self):
        print('bar in adaptee')


class adapter(object):
    def __init__(self):
        self.adaptee = adaptee()

    def foo(self):
        print('foo in adapter')
        self.adaptee.foo()

    def __getattr__(self, name):
        return getattr(self.adaptee, name)


class lazy_attribute(object):
    """ A property that caches itself to the class object. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter = func

    def __get__(self, obj, cls):
        value = self.getter(cls)
        setattr(cls, self.__name__, value)
        return value


class Widget(object):
    @lazy_attribute
    def complex_attr_may_not_need(clz):
        print('complex_attr_may_not_need is needed now')
        return sum(i * i for i in range(1000))


class WidgetShowLazyLoad(object):
    def fetch_complex_attr(self, attrname):
        '''可能是比较耗时的操作， 比如从文件读取'''
        return attrname

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = self.fetch_complex_attr(name)
        return self.__dict__[name]


if __name__ == '__main__':
    w = WidgetShowLazyLoad()
    print('before', w.__dict__)
    w.lazy_loaded_attr
    print('after', w.__dict__)
