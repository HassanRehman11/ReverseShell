import socket
import sys
import os
import subprocess

host="127.0.0.1"
port=9898
s = socket.socket()
s.bind((host, port))
s.listen(5)
conn, address = s.accept()
print("Connected at::: " + "IP " + str(address[0]) + " | Port " + str(address[1]))

while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
conn.close()