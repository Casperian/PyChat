# Echo server program
from win32api import GetSystemMetrics
import socket, select, random
from tkinter import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
loop = 0
gotuser = 0
def getuser():
    global gotuser
    global username
    usernamesuffix = str(random.randint(1000,9999))
    tempuser = userBox.get()
    if tempuser == "":
       Lb1.insert(0, "Please Select a Username")
    else:
        gotuser = 1
        username = tempuser + "." + usernamesuffix

def recieveData():
    global loop
    if loop > 10:
        loop = 0
    try:    
        ready = select.select([s], [], [], 0)
        if ready[0]:
            data = s.recv(4096)
            data2 = data.decode('utf-8')
            if data:
                    Lb1.insert(loop, data2)
                    loop = loop + 1
        app.after(1, recieveData)
    except:
        print("Socket Down")
def closeapp():
    try:
        s.shutdown(socket.SHUT_WR)
        exit()
    except:        
        exit()

def sendData():
    text = str(entryBox.get())
    text2 = "<" + username + ">" + text
    text3 = text2.encode('utf-8')
    s.sendall(text3)

def connserver():
    if gotuser == 0:
        getuser()
    connection = connectBox.get()
    if ":" in connection:
        param, value = connection.split(":",1)
        PORT = value
        HOST = param
    else:
        HOST = connection
        PORT = 20202             # The same port as used by the server
    try:
        s.connect((HOST, PORT))
        welcome = username + " joined the chat"
        welcome = welcome.encode('utf-8')
        s.sendall(welcome)

    except:
        Lb1.insert(0, "Connection Failed")
        raise



app = Tk()
app.title("")
app.resizable(0,0)
width = (GetSystemMetrics(0))//2
height = (GetSystemMetrics(1))//2
res = str(width) + 'x' + str(height)
app.geometry(res)

connectBox = Entry(app)
connectBox.place(x=60,y=25)

connButton = Button(app, text = "Connect", command = connserver)
connButton.place(x=0,y=50)

entryBox = Entry(app,width=145)
entryBox.place(x=10,y=(height-80))

sendButton = Button(app, text = "Send", command = sendData)
sendButton.place(x=(width-60),y=(height-85))

Lb1 = Listbox(app, height=20, width=150)
Lb1.place(x=20,y=100)

recieveData()
userBox = Entry(app)
userBox.place(x=60,y=0)
userBox.focus_set()

userlabel = Label(app, text="Username").place(x=0,y=0)

serverlabel = Label(app, text="Server").place(x=0,y=25)

closeButton = Button(app, text = "Release", command = closeapp)
closeButton.place(x=(width-60),y=(height-40))

app.mainloop()

