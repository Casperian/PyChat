# Echo client program
import socket

def client():
    try:
        connect=1
        while True:
            try:
                HOST = "172.16.190.4"   # The remote host
                PORT = 50007              # The same port as used by the server
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                break
            except:
                print("finding connection",connect,"tries")
                connect=connect+1
        print("Enter your name")
        while 1==1:
            try:
                name=str(input())
                break
            except:
                print("retry")
        send=(name + " has connected")
        send=send.encode('utf-8')
        s.sendall(send)
        print("You are now in chat:")
        print("type 'exit' to exit")
        while True:
            send=input()
            if send=="exit":
               break
            send=(name+':'+send)
            send=send.encode('utf-8')
            s.sendall(send)
        s.close()
    except:
        print("An error occured you have been disconeccted")
        s.close()

def server():
    print("SERVER DOESNT EXIST YET")

while True:
    print()
    print("1. Client")
    print("2. Server")
    g=input()
    if g=="1" or g=="client" or g=="Client":
        client()
    if g=="2" or g=="server" or g=="Server":
        server()

        
