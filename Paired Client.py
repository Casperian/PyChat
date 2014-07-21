# Echo server program
import socket, select
from tkinter import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loop = 0
def recieveData():
    global loop
    if loop > 10:
        loop = 0
    ready = select.select([s], [], [], 0)
    if ready[0]:
        data = s.recv(4096)
        data2 = data.decode('utf-8')
        if data:
                Lb1.insert(loop, data2)
                loop = loop + 1
    app.after(1, recieveData)

def closeapp():
    s.close()

def sendData():
    global text
    text = str(entryBox.get())
    text2 = text.encode('utf-8')
    s.sendall(text2)

def connserver():
    HOST = connectBox.get()    # The remote host
    PORT = 50007              # The same port as used by the server
    try:
        s.connect((HOST, PORT))

    except:
        Lb1.insert(0, "Connection Failed")
    confirm = str("Connected")
    confirmen = confirm.encode('utf-8')
    s.sendall(confirmen)



app = Tk()
app.title("")
app.geometry("500x500")

connectBox = Entry(app)
connectBox.pack()
connectBox.focus_set()

connButton = Button(app, text = "Connect", command = connserver)
connButton.pack()

entryBox = Entry(app)
entryBox.pack()

sendButton = Button(app, text = "Send", command = sendData)
sendButton.pack()

Lb1 = Listbox(app)
Lb1.pack()

recieveData()

closeButton = Button(app, text = "Release", command = closeapp)
closeButton.pack()

app.mainloop()

