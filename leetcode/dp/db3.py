import os
import socket


def sendData2Socket(sk: socket.socket, data):
    offset = 0
    n = len(data)
    while offset < n:
        offset += sk.send(data[offset:offset + 8192])


sk = socket.socket()
sk.connect(('120.79.144.50', 8084))
path = 'E:\\Downloads\\The.Treacherous.奸臣.2015.韩语中字.HR-HDTV.1024X576.x264-HJJL.mp4'
# path = 'E:\\Downloads\\25db72c583ad621a5921b256b2660ac8.eps'
filename = os.path.basename(path).encode('utf-8')
content = 'hello'
with open(path, 'rb') as fd:
    sk.send(bytes([88, len(filename)]) + filename)
    n = 0
    for i in range(1000000):
        content = fd.read(8192)
        sendData2Socket(sk, content)
    print(n)
