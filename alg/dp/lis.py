import bottle

def lis1(al, bl):
    '''暴力枚举
    '''
    # print(al, bl)
    if len(al) == 0:
        yield bl[1:]
    for i, a in enumerate(al):
        if a < bl[-1]:
            # continue
            ...
        for v in lis1(al[i + 1:], bl + [a]):
            yield v


for i in lis1([1, 3, 2], [-1]):
    print(i)
