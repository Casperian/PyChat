# Echo server program
import socket
from tkinter import *
print(socket.gethostbyname(socket.gethostname()))
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

def recieveData():
    global data
    data = conn.recv(1024)
    data2 = data.decode('utf-8')
    if data:
        print(data2)
    app.after(1, recieveData)

def closeapp():
    conn.close()

def sendData():
    global text
    text = str(entryBox.get())
    text.encode('utf-8')
    conn.sendall(text)




app = Tk()
app.title("")

entryBox = Entry(app)
entryBox.pack()

sendButton = Button(app, text = "Send", command = sendData)
sendButton.pack()

recieveData()

app.mainloop()


