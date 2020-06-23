import socket
import struct
import json
import os

buffer = 1024
sk = socket.socket()
sk.bind(('127.0.0.1',9980))
sk.listen()
conn,addr = sk.accept()

head_size = conn.recv(4)
head_size = struct.unpack('i',head_size)[0]

json_head = conn.recv(head_size).decode('utf-8')

head = json.loads(json_head)    #head = <class 'dict'>


filesize = head['filesize']

head_server ={'filepath':r'C:\Users\Tianqi\Desktop'}
head_path = os.path.join(head_server['filepath'],head['filename'])
with open(head_path,'wb') as f:

    while filesize:
        if filesize >= buffer:
            content = conn.recv(buffer)
            f.write(content)
            filesize -= buffer
        else:
            content = conn.recv(filesize)
            f.write(content)
            break
conn.close()
sk.close()



