import socket
import json
import os
import struct

sk = socket.socket()
sk.connect(('127.0.0.1',9980))

buffer = 1024
head = {
    'filepath':r'C:\Users\Tianqi\Desktop\myfile',
    'filename':r'MKZ密码.pdf',
    'filesize':None
}

headpath = os.path.join(head['filepath'],head['filename'])
headsize = os.path.getsize(headpath)
head['filesize'] = headsize



json_head = json.dumps(head)
byte_head = json_head.encode('utf-8')

head_len = len(byte_head)
head_size = struct.pack('i',head_len)

sk.send(head_size)
sk.send(byte_head)
with open(headpath,'rb') as f:
    while headsize:
        if headsize >= buffer:
            content = f.read(buffer)
            sk.send(content)
            headsize -= buffer
        else:
            content = f.read(buffer)
            sk.send(content)
            break

sk.close()










