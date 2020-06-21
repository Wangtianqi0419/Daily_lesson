import socket
sk = socket.socket()

sk.bind(('127.0.0.1',8999))
sk.listen()
conn,addr = sk.accept()

while 1:
    cmd = input('>>>>').encode('gbk')
    if cmd == 'q':
        conn.send(b'q')
        break
    conn.send(cmd)
    num = conn.recv(1024).decode('utf-8')
    conn.send(b'ok')

    res = conn.recv(int(num)).decode('gbk')
    print(res)
conn.close()
sk.close()
