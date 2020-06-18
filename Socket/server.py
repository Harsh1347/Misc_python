import socket 
 
HEADERSIZE = 10

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True : 
    clientsocket,address=s.accept() 
    print(f"You have established connection with {address}")
    
    msg  = 'Welcome to the server'
    print(f'{len(msg):<{HEADERSIZE}}'+msg)
    
    clientsocket.send(bytes(msg,"utf-8"))
    
    