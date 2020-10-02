import socket

s1 = socket.socket()


hostname = "127.0.0.1"
port = 5656


s1.bind((hostname, port))
s1.listen(1)

client, addr = s1.accept()

word = client.recv(1000)
word = "hello "+word.decode("utf-8")

import prasad
ob = prasad.Ravi()
res = ob.Display()


result = bytes(res, "utf-8")
client.send(result)
