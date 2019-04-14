import socket
import sys
import struct


def send():
    host, port, file = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    with open(file, 'rb') as fd:
        s = fd.read()
    sk = socket.socket()
    sk.connect((host, port))
    sk.send(struct.pack('>l', len(s)) + s)


if __name__ == '__main__':
    print(struct.unpack('>l', b'\x00\x00\x05\x9b'))
