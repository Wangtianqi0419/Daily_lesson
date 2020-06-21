import socket
import subprocess
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',8999))

while 1:
    cmd = sk.recv(1024).decode('gbk')

    res = subprocess.Popen(cmd,shell=1,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    std_out = res.stdout.read()
    std_err = res.stderr.read()
    num_by = len(std_out)+len(std_err)
    len_by = struct.pack('i',num_by)   # 把将要发送的数据字节大小 转换成四字节
    sk.send(len_by)  # 将此文件的大小发送出去
    sk.send(std_out)
    sk.send(std_err)

sk.close()




