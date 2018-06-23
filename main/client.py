from socket import  *
import  socket
def clicent():
    host="127.0.0.1"
    port=58
    addr=(host,port)
    s=socket.socket(AF_INET,SOCK_STREAM)
    s.connect(addr)
    while True:
        print("''''''")
        data=input('>')
        if not  data:
            s.send(data)
            data=s.recv(1024)
        if not data:
              break
              print(data)
    s.close()
clicent()
