import typing

'''
333
332
331
323
322
321
'''

arr = [0, 0, 0]


def compose(n: int, x: int):
    '''
    example: 
    '''
    if x == 1:
        for i in range(1, n + 1):
            yield [i]
        return
    for i in compose(n, x - 1):
        for j in range(1, n + 1):
            yield i + [j]


def permutations(ary: typing.List[int]):
    if len(ary) == 1:
        yield ary
        return
    for item in permutations(ary[:-1]):
        for i in range(len(ary)):
            yield item[:i] + [ary[-1]] + item[i:]


if __name__ == "__main__":
    # for i in compose(3, 3):
        # print(i)
    for i in permutations([1, 2, 3]):
        print(i)
