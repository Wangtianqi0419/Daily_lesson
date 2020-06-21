import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

sk.bind(('127.0.0.1',9090))

conn,addr = sk.recvfrom(1024)
print(conn.decode('utf-8'))
sk.sendto(b'bye',addr)

sk.close()