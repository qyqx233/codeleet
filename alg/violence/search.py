# 8 0 0
import typing
from collections import namedtuple

FromTo = namedtuple("FromTo", ["from1", "to", "vol"])


def water(vols: typing.List[int]):
    bulk = [0 for i in range(1000)]

    def checkValid(cols: typing.List[int]):
        index = 100 * cols[-3] + 10 * cols[-2] + cols[-1]
        if bulk[index] == 1:
            return False
        bulk[index] = 1
        return True

    def fromTo(vols: typing.List[int], ):
        vv = [[0, 8], [1, 5], [2, 3]]
        for i, v in enumerate(vols):
            for j, v1 in enumerate(vols):
                if j == i:
                    continue
                if v < vv[i] and v1 > 0:
                    yield FromTo(j, i, min(v, v1))
    if vols[0] == 4 or vols[1] == 4 or vols[2] == 4:
        return
    for ft in fromTo(vols):
        vols1 = [i for i in vols]
        vols1[ft.from1] -= ft.vol
        vols1[ft.to] += ft.vol
        if not checkValid(vols1):
            return
        water(vols1)
    print(vols)
