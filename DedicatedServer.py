# Echo server program
import socket,select
from datetime import datetime
from tkinter import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 20202            # Arbitrary non-privileged port
userlist = []

try:
    with open("MOTD.txt", 'rb') as fo:
        motd = fo.read()
except:
    print("Error with MOTD.txt - Does it exist?")
    motd = "Hello User"
    motd = motd.encode('utf-8')
    
hlplst = []
hlplst.append("Commands are proceded by a /")
hlplst.append("Currently the working commands are;")
hlplst.append("/ip")
hlplst.append("/about")


print("Server IP")
print(socket.gethostbyname(socket.gethostname())+ ":" + str(PORT))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
userlist.append(s)

#Function to broadcast chat messages to all connected clients
def broadcast (read, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in userlist:
        if socket != s: # and socket != read :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                userlist.remove(socket)

def wlcmusr (read, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in userlist:
        if socket != s and socket != read :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                userlist.remove(socket)                
try:
    while True:
        read_sockets,write_sockets,error_sockets = select.select(userlist,[],[])
        for read in read_sockets:
            if read == s:
                conn, addr = s.accept()
                print("New User: " + str(addr))
                userlist.append(conn)

            else:
                try:
                    data = read.recv(8192)
                    if data:
                        dedata = data.decode('utf-8')
                        if ">" in dedata:
                            param, value = dedata.split(">",1)
                            if value == "/ip":
                                ip = "IP: " + socket.gethostbyname(socket.gethostname())
                                ip = ip.encode('utf-8')
                                read.send(ip)

                            elif value == "/help":
                                for i in range(0,4):
                                    hlpmssg = hlplst[i]
                                    hlpmssg = hlpmssg.encode('utf-8')
                                    read.send(hlpmssg)
                                    time.sleep(0.05)

                            elif value == "/about":
                                about = "PyChat Server Version 0.9.18.428" 
                                about = about.encode('utf-8')
                                read.send(about)





                                
                            else:
                                ctime = str(datetime.now().time())
                                ctime = "[" + ctime[:5] + "] "
                                ctime = ctime.encode('utf-8')
                                transdata = ctime + data
                                with open("Log.txt", 'wb') as fo:
                                    fo.write(transdata)
                                broadcast(read,transdata)

                        else:
                            ctime = str(datetime.now().time())
                            ctime = "[" + ctime[:5] + "] "
                            ctime = ctime.encode('utf-8')
                            transdata = ctime + data                            
                            read.send(motd)
                            wlcmusr(read,transdata)

                except:
                    print("Connection Error from client", read)
                    read.close()
                    userlist.remove(read)
                    continue
except(KeyboardInterrupt):
    print("Shutting down at user command")
    s.shutdown(Socket.SHUT_WR)
    time.sleep(1)
    s.close()





