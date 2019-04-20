import array

bs = b'sssss'
mb = memoryview(bs)
# mb[0] = 100
for i in mb:
    print(type(i), i)

for i in bs:
    print(type(i), i)

print(array.array('I', [100, 200]))
