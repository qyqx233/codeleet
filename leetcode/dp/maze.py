import typing

# 机器人只能向右，向下行走，列出所有可能
def xoo(m: int, n: int, arr: typing.List[int]):
    # print(m, n, arr)
    if m == 1 and n == 1:
        print(arr)
        return
    # print(m, n)
    if m > 1:
        arr1 = arr.copy()
        arr1.insert(0, 1)
        xoo(m - 1, n, arr1)
    if n > 1:
        arr2 = arr.copy()
        arr2.insert(0, 2)
        xoo(m, n - 1, arr2)

