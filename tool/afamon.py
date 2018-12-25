import os


def getProcessInfo():
    for i, j, k in os.walk('D:\\Applicatio\\opencv\\build\\include'):
        for f in k:
            pathName = os.path.join(i, f)
            if not os.path.isfile(pathName):
                continue
            with open(pathName) as fd:
                s = fd.read()
            if s.lower().find('getstructuringelement') >= 0:
                print(pathName)


getProcessInfo()
