s1 = "hello"
s2 = "hello"
print(s1 is s2)


# 如果有空格，默认不启用intern机制
s1 = "hell o"
s2 = "hell o"
print(s1 is s2)

# 如果一个字符串长度超过20个字符，不启动intern机制
s1 = "a" * 20
s2 = "a" * 20
print(s1 is s2)

s1 = "a" * 21
s2 = "a" * 21
print(s1 is s2)

s1 = "ab" * 10
s2 = "ab" * 10
print(s1 is s2)

s1 = "ab" * 11
s2 = "ab" * 11
print(s1 is s2)

s1 = "hell"
s2 = "hello"
print(s1 + "o" is s2)  # False
print("hell" + "o" is s2)  # True
