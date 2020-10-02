import socket

c1 = socket.socket()

hostname = "127.0.0.1"
port = 5656

c1.connect((hostname,port))


name = "RaviPrasad"
name = bytes(name, "utf-8")

c1.send(name)

result = c1.recv(100)
result = result.decode("utf-8")
print(result)
