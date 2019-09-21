import functools
import itertools
import typing


def getMax(ccys, ccyNums: typing.List[int]):
    for i in range(len(ccyNums) - 1, -1, -1):
        if ccyNums[i] >= 0:
            break
    else:
        return i, ccys[i]
    return -1, 0


def aa(ccys: typing.List[int], ccyNums: typing.List[int], target: int) -> int:

    # total = 0
    # while True:
    #     lst = ccys.copy()
    #     break
    pass


print(list(range(3, -1, -1)))
