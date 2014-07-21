# Echo server program
import socket,select
from tkinter import *
print("Server IP")
print(socket.gethostbyname(socket.gethostname()))
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()


while True:
    ready = select.select([conn], [], [], 0)
    if ready[0]:
        data = conn.recv(8192)
        if data:
            conn.sendall(data)

conn.close()





