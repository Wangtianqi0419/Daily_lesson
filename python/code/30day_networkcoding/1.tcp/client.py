import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8080))

while 1:
    info = input('>>>').encode('utf-8')
    sk.send(info)
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'bye':
        sk.send(b'bye')
        break
    print(ret)
