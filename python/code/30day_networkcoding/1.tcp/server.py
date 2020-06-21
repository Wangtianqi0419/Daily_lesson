import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8080))

sk.listen()
conn,addr = sk.accept()
while 1 :
    ret = conn.recv(1024).decode('utf-8')
    if ret == 'bye':
        conn.send(b'bye')
        break
    print(ret)
    info = input('>>>>').encode('utf-8')
    conn.send(info)
