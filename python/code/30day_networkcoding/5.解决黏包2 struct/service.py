import socket
import struct
sk = socket.socket()

sk.bind(('127.0.0.1',8999))
sk.listen()
conn,addr = sk.accept()

while 1:
    cmd = input('>>>>').encode('gbk')    #根据操作的机器系统来选择编码
    if cmd == 'q':
        conn.send(b'q')
        break
    conn.send(cmd)
    num = conn.recv(4)  #收到转换后四字节数
    num = struct.unpack('i',num)[0]  #将四字节的bytes数转换为 str 类型
    # print(type(num))
    # num_by = struct.unpack(conn.recv(4))
    res = conn.recv(num).decode('gbk')
    print(res)
conn.close()
sk.close()
