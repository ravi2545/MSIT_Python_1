import mysql.connector
import json
class Databases:
    def db_connect(self,email,password):
        self.myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Ravi@143", database = "kalyan")
        self.cur = self.myconn.cursor()
        s = "INSERT INTO user(email,password) VALUES(%s,%s)"
        t = (email,password)
        self.cur.execute(s,t)
        self.myconn.commit()
    def fetch(self, mn, ps):
        data = mn,ps
        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="kalyan")
        self.cur = self.myconn.cursor()
        self.cur.execute("select * from user")
        res = self.cur.fetchall()
        self.myconn.close()
        if data in res:
            return json.dumps(res)

    def Raw_data(self):
        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="kalyan")
        self.cur = self.myconn.cursor()
        self.cur.execute("select * from user")
        res = self.cur.fetchall()
        self.myconn.close()
        return res
