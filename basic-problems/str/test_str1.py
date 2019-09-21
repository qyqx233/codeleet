def Test_splitChar():
    print(splitStr("abc,,de", ","))
    print(splitStr("abc,de,", ","))
    print(splitStr(",abc,de,", ","))

l = [1, 2]
del l[1:]
print(l)