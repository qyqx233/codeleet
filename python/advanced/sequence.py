import collections
import types


def foo():
    pass


print(isinstance(foo, types.FunctionType))
print(issubclass(list, collections.MutableSequence))
print(issubclass(tuple, collections.MutableSequence))

[i for i in range(100)]
print(i)