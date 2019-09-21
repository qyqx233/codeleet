from typing import List


def minLenPath(arr: List[List[int]]) -> int:
    arr1 = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr) - 1, -1):
        for j in range(len(arr[0])):
            if i == len(arr) - 1:
                if j == 0:
                    arr1[i][j] = arr[i][j]
                else:
                    arr1[i][j] = arr[i][j] + arr1[i][j - 1]
            else:
                if j == 0:
                    arr1[i][j] = arr[i - 1][j] + arr1[i][j]
                else:
                    arr1[i][j] = min(arr1[i - 1][j], arr1[i]
                                     [j - 1]) + arr[i][j]
    return arr1[0][-1]


# minLenPath([[]])
