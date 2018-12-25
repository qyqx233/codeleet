import typing


def maxLenSubQueue(q: typing.List) -> typing.Tuple[int, typing.List]:
    if len(q) == 1:
        return 1, q[0], q[0]
    last = q[-1]
    n, mn, mx = maxLenSubQueue(q[:-1])
    if last > mx:
        mx = last
        n += 1
    elif last < mn:
        mn = last
        n += 1
    
    return n, mn, mx


if __name__ == "__main__":
    print(maxLenSubQueue([4, 2, 4, 2, 5, 6]))
