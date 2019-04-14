class Clz():
    def __getattribute__(self, key):
        print('__getattribute__ ' + key)
        return object.__getattribute__(self, key)

    def __getattr__(self, item):
        return 'fuck'


c = Clz()
c.a = 100
print(c.b)
