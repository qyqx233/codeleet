Container sequences
    `list, tuple, and collections.deque`
Flat sequences
    `str, bytes, bytearray, memoryview, and array.array` hold items of one type

`Container sequences hold references to the objects they contain, which may be of any
type, while flat sequences physically store the value of each item within its own memory
space, and not as distinct objects. Thus, flat sequences are more compact, but they are
limited to holding primitive values like characters, bytes, and numbers.`

`Container:__contains__, Iterable:__iter__, Sized:__len__`
`Sequence: __getitem__, __containcs__, __iter__, __reversed__, index, count`

`sorted` & `list.sort`

The list.sort method sorts a list in place—that is, without making a copy

In fact, it accepts any iterable object as an argument, including immutable sequences and generators