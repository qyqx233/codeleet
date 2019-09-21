def isPalindrome(s: str):
    leng = len(s)
    start, end = 0, leng - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True



