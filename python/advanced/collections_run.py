import collections
import json

Student = collections.namedtuple('Student', "name sex age")
helen = Student("helen", 'f', 10)
print(helen.name)


dq = collections.deque(maxlen=2)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)


orderDict = collections.OrderedDict()
orderDict['b'] = 100
orderDict['a'] = 50
print(json.dumps(orderDict))

mp1 = {'a': 100}
mp2 = {'a': 200, 'b': 300}
chainMap = collections.ChainMap(mp1, mp2)
print(chainMap['a'], chainMap['b'])

defaultDict = collections.defaultdict(int)
print(defaultDict['a'])

counter = collections.Counter('abcdef')
print(counter)
