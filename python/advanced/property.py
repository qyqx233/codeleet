
class Test(object):
    def __init__(self):
        self.__num = 0

    def getNum(self):
        print('----get----')
        return self.__num

    def setNum(self, newNum):
        print('----set----')
        self.__num = newNum

    num = property(getNum, setNum)


class Test1(object):
    def __init__(self):
        self.__num = 0

    @property
    def num(self):
        print('----get----')
        return self.__num

    @num.setter  # 两个方法名要相同,用 方法名.setter 声明设置它的方法.
    def num(self, newNum):
        print('----set----')
        self.__num = newNum
