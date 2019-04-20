import typing


def foo(al: typing.List[int]):
    bl = [1 if i % 2 == 1 else 0 for i in al]
    i, j = 0, len(al) - 1
    while i < j:
        if bl[i] == 0:
            while j >= 0 and bl[j] != 1:
                j -= 1
            if j == -1:
                break
            al[i], al[j] = al[j], al[i]
            j -= 1
        i += 1


al = [8, 1, 6, 4, 3, 2, 5, ]
foo(al)
print(al)
