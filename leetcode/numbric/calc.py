import typing
import itertools


def fourNum(nums: typing.List[int], target: int):
    for i in itertools.combinations(nums):
        print(i)


def threeNum(nums: typing.List[int], target: int):
    pass


def twoNum(nums: typing.List[int], target: int):
    mp = {i: target - i for i in nums}
    for i, j in mp.items():
        if j in nums:
            print(i, j)


if __name__ == "__main__":
    twoNum([1, 2, 3, 4, 7, 6], 10)
