import  socket
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',9090)
info = '我的世界'
sk.sendto(info.encode('utf-8'),ip_port)

msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))


