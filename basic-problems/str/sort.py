def select_sort(lst: list):
    '''选择排序
    '''
    leng = len(lst)
    for i in range(leng):
        min, pos = lst[i], i
        for j in range(i + 1, leng):
            if lst[j] < min:
                min, pos = lst[j], j
        lst[i], lst[pos] = lst[pos], lst[i]


def bubble_sort(lst: list):
    '''冒泡排序
    '''
    leng = len(lst)
    for i in range(leng - 1, -1, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lst = [2, 2, 3, 1]
bubble_sort(lst)
print(lst)
