import socket

s1 = socket.socket()


hostname = "127.0.0.1"
port = 5656

s1.bind((hostname, port))
s1.listen(1)


client,addr = s1.accept()

word = client.recv(1000)
word = word.decode("utf-8")

import poem
p1 = poem.Poem()
p1.clean()

result = p1.getAllTheLines(word)
result = result[1:]
total_lines = len(result)

from xml.dom.minidom import Document
doc = Document()

lines = doc.createElement("lines")
lines.setAttribute("word",word)
lines.setAttribute("total", str(total_lines))

for line_number, actual_line in result:
    line = doc.createElement("line")
    line.setAttribute("line_number",str(line_number))

    text = doc.createTextNode(actual_line)
    line.appendChild(text)
    lines.appendChild(line)
doc.appendChild(lines)

final_result = doc.toxml()
final_result = bytes(final_result, "utf-8")

client.send(final_result)


