import socket

#To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax −
s1 = soket.socket()



hostname = "127.0.0.1"  
port = 5656 #a port is a logical construct that identifies a specific process or a type of network service


#This method binds address (hostname, port number pair) to socket.
s1.bind((hostname, port))
s1.listen(1) #The listen function places a socket in a state in which it is listening for an incoming connection.

clinet, addr  = s1.accept()#This passively accept TCP client connection, waiting until connection arrives (blocking).


word = client.recv(1000)

word = word.decode("utf-8")

result = bytes(res, "utf-8")
client.send(result)
