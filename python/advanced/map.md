Python官方文档中对于一个对象是否可哈希（Hashable）
>An object is hashable if it has a hash value which never changes during its lifetime (it needs a hash()method), and can be compared to other objects (it needs an eq()or cmp()method). Hashable objects which compare equal must have the same hash value.

Python中内建的Hashable对象包括：str、bytes、数字类型、frozenset等immutable对象，所有的可变序列对象都不是可哈希的，对于tuple则仅当其中所有的元素都是Hashable对象时才是可哈希的。用户自定义的对象通常是可哈希的，这是因为这些对象的 `__hash__()`方法默认返回的是该对象的id（即`id(obj)`返回的值），而一个对象的id是唯一的

mapping对象中对于 `mapObj[key]` 这个语法的支持本质上是调用 `mapObj.__getitem__(key)` 方法，但是当 `__getitem__(key)` 方法无法找到key的时候，mapObj对象的 `__missing__(key)` 方法就会被调用。

`__missing__()` 方法的调用仅仅会由 `mapObj[key]` 这个语法来触发，而 `mapObj.get(key, default)` 这个方法的调用是不会触发__missing__方法的

如果需要保持这些 key:value 对插入的顺序，则需要使用 `collections.OrderedDict` 类

用户自定义类dict的class的时候，通常不要直接以dict作为父类，这是因为在覆盖重写`dict类的 get(k, default),__setitem__(), __contain__(), __missing__()` 等方法时，常常又会使用到 `mapObj[k]、 k in mapObj、mapObj[k]` 等语法形式，这样一不小心就会造成这些内部方法的无穷递归调用。因此更建议使用 `collections.UserDict` 类而非dict来作为自定义mapping的父类

collections.UserDict 名字中包含"dict"，但是它并不是dict的子类，而是 collections.MutableMapping 的子类，因此UserDict类也继承了 `__getitem__(), __contain__(), __setitem__()` 等方法。UserDict类与dict的关联是通过UserDict对象中包含一个dict类型的成员变量 data 来实现的，data就作为真正的dict数据内容的保存地。用户自定义类dict class覆盖重写这些方法的时候，并不会递归调用UserDict类中其他的方法，而是对UserDict.data 变量进行相关操作，从而大大减轻了用户自定义类时对于死循环递归的防范难度

set和frozenset 中每一个元素都是唯一而不重复的，这样的唯一性正是通过每个元素对象的hash值唯一来保证的，因此:
1. set和frozenset中每一个元素对象必须是Hashable对象
2. set本身不是Hashable对象（因为set是mutable对象）
3. frozenset本身是immutable 对象，因此其本身也是Hashable对象
