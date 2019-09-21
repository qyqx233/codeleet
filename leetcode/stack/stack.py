# 进制转换
def jzzh(n: int, b: int) -> str:
    x = n
    lst = []
    while x > 0:
        x, y = divmod(x, b)
        lst.append(y)
    return ''.join((str(i) for i in lst[::-1]))


# 判断括号是否闭合
def checkKh(s: str) -> bool:
    stack = []
    for i, c in enumerate(s):
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']':
            c1 = stack.pop()
            if c1 != {'}': '{', ']': '[', ')': '('}[c]:
                return False
    return True


# 耦合
class SimulateFIFO():
    pass


if __name__ == "__main__":
    # print(jzzh(17, 2))
    print(checkKh("(({)})((a=1)and(b=2))"))
