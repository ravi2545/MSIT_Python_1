import socket## Import socket module

c1 = socket.socket()

hostname = "127.0.0.1"
port = 5656

c1.connect((hostname, port))#This method actively initiates TCP(Transmission Control Protocol) server connection.

name = "land"
name = bytes(name, "utf-8")

c1.send(name)

result = c1.recv(1000)
result = result.decode("utf-8")
print(result)

