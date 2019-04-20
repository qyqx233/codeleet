## 序列的分类

从序列中的元素类型是否一致作为标准，可分为容器序列(Container sequences包括list, tuple, collections.deque)和固定序列(Flat sequences，包括str、bytes、bytearray、memoryview、array.array)

容器序列中实际存放的元素是对其他任意对象的引用，而固定序列中存放是真正的是元素值，因此所有的元素必须是相同类型，并且只能是Python基本类型（字符、字节、数字等）的数据。

从序列中的元素是否能够被修改的标准来看，Python的序列类型又分为可变序列(Mutable sequences，包括list、bytearray、array.array、collections.deque、memoryview等)和不可变序列(Immutable sequences，包括tuple、str、bytes等)

## 生产序列的方法

列表推导和生成器表达式


