
import socket
import os
import json


client = socket.socket()
client.connect(('localhost',9000))

while True:
    choice = input(">>>").strip()
    if len(choice) == 0:continue
    client.send(choice.encode())
    recv = client.recv(1024)

    print("received:",recv.decode())

