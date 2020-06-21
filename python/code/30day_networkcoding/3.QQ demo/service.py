
import socket
ip_port= ('127.0.0.1',9000)
sk = socket.socket(type=socket.SOCK_DGRAM)

msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))

sk.sendto(b'nininiainia',addr)

sk.close()