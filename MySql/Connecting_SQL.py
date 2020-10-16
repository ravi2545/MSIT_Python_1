import mysql.connector


class MY_DataBase:
    def __init__(self):
        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143")
        self.cur = self.myconn.cursor()

    def Show_databases(self):
        database = []
        try:
            dbs = self.cur.execute("show databases")
        except:
            self.myconn.rollback()

        for data in self.cur:
            for k in data:
                database.append(k)
        self.myconn.close()
        return database


    def Connect_database(self, mydatabase):
        result = self.Show_databases()
        if mydatabase in result:
            my_new_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Ravi@143", database = mydatabase)
            return my_new_conn
        else:
            try:
                self.cur.execute("create database {}".format(mydatabase))
            except:
                self.myconn.rollback()
            return "Created Database Please connect"

    def Databases(self):
        database_name = "kalyan"
        tables_Name = self.Connect_database(database_name)
        try:
            table = self.cur.execute("show tables")
        except:
            self.myconn.rollback()
        for x in self.cur:
            print(x)




mydatabase = 'kalyan'
obj = MY_DataBase()
#print(obj.Show_databases())
#print(obj.Connect_database(mydatabase))
print(obj.Databases())