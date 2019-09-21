def splitStr(s: str, splitChar: str):
    '''分割字符串
    splitChar('ab,c', ',') -> ['ab', 'c']
    '''
    word, lastChar, lst = '', False, []
    for i in s:
        if i not in splitChar:
            if lastChar:
                word += i
            else:
                word = i
            lastChar = True
        else:
            if word:
                lst.append(word)
                word = ''
            lastChar = False
    else:
        if word:
            lst.append(word)
    return lst


