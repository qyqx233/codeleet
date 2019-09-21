import logging
logging.basicConfig(level=logging.DEBUG, format='%(lineno)04d:%(message)s')


def isMatch(s: str, p: str) -> bool:
    '''leetcode 44
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    完全匹配才算匹配
    '''
    # total = 0
    # rmk = [0] * len(p)
    # for i in range(len(p) - 1, -1, -1):
    #     if p[i] != '*':
    #         total += 1
    #     rmk[i] = total
    logging.debug('%s %s', str(s), str(p))
    if len(p) == 1 or p == '':
        if p == '*':
            return True
        elif p == '?':
            if len(s) == 1:
                return True
            else:
                return False
        else:
            return s == p
    if s == '':
        if p.count('*') == len(p):
            return True
        else:
            return False
    if p[0] == '*':
        return any([isMatch(s[i:], p[1:]) for i in range(len(s))])
    elif p[0] == '?':
        return any([isMatch(s[1:], p[1:]) for i in range(1, len(p))])
    else:
        if s[0] != p[0]:
            return False
        return any([isMatch(s[1:], p[1:]) for i in range(1, len(p))])


def test_isMatch():
    # assert(isMatch('axb', 'a*b'))
    # assert(isMatch('axb', '*a*b'))
    # assert(isMatch('xabaca', '*a'))
    # assert(isMatch('xabaca', '*a?a'))
    assert(isMatch('aa', 'aa**'))


test_isMatch()
