from a import isPalindrome


def test_isPalindrome():
    assert(isPalindrome("a") is True)
    assert(isPalindrome("ab") is False)
    assert(isPalindrome("aba") is True)
    assert(isPalindrome("abba") is True)
    assert(isPalindrome("abbaa") is False)


# test_isPalindrome()
lst = [2]
lst.insert(0, 1)
print(lst)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mx = [[0] * m for i in range(n)]
        for x in range(m):
            for y in range(n):
                if y == 0:
                    mx[y][x] = 1
                elif x == 0:
                    mx[y][x] = 1
                else:
                    mx[y][x] = mx[y - 1][x] + mx[y][x - 1]
        return mx[n - 1][m - 1]


Solution().uniquePaths(3, 2)
