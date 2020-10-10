import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="kalyan")
cur=mycon.cursor()
cur.execute("CREATE database kalyan")
print("DabaBase Created")
mycon.close