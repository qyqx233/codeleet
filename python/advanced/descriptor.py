
import functools
import time


class cached_property(object):
    """ A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property. """

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class TestClz(object):
    @cached_property
    def complex_calc(self):
        print('very complex_calc')
        return sum(range(100))


if __name__ == '__main__':
    t = TestClz()
    print('>>> first call')
    print(t.complex_calc)
    print('>>> second call')
    print(t.complex_calc)
