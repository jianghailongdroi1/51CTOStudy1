

import socket
import json
s = socket.socket()
s.bind(('localhost',9000))

s.listen(5)

while True:
    conn,client_addr = s.accept()
    print("got a new conn:",client_addr)

    while True:
        data = conn.recv(1024)
        print("recv data:",data)
        data = json.loads(data.decode())

        if data.get('action') is not None:
            if data['action'] == "put":
                #client sends file to server
                file_obj = open(data["filename"],"wb")
                received_size = 0

                while  received_size < data["size"]:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    received_size += len(recv_data)
                    print(data['size'],received_size)
                else:
                    print("---successfully received file [%s]---", data['filename'])
                    file_obj.close()

         elif data['action'] == "get":
                # client downloads file from  server
                pass




