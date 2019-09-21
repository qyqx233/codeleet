import types


def foo():
    for i in range(10):
        yield i


print('__next__' in dir(foo))
print(type(foo()))
print(isinstance(foo(), types.GeneratorType))
