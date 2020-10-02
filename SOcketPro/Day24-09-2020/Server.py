import socket
import threading


class Mythread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        name = client.recv(100)
        name = name.decode("utf-8")
        name = "hello"+name
        name = bytes(name, "utf-8")

        self.client.send(name)
        

s1 = socket.socket()
hostname = "127.0.0.1"
port = 5656
s1.bind((hostname, port))
s1.listen(1)
while True:
    client,addr = s1.accept()
    t1 = Mythread(client)
    t1.start()
