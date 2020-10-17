import mysql.connector


class MY_DataBase:
    def __init__(self):
        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database="kalyan")
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
            my_new_conn = mysql.connector.connect(host="localhost", user="root", passwd="Ravi@143", database=mydatabase)
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

    def Table_data(self):
        tables = []
        try:
            table_info = self.cur.execute("show tables")

        except:
            self.myconn.rollback()

        for i in self.cur:
            for data in i:
                tables.append(data)

        self.myconn.close()
        return tables

    def show_data(self, tname):
        data = []
        try:
            self.cur.execute("SELECT * FROM {}".format(tname))
        except:
            self.myconn.rollback()
        res = self.cur.fetchall()
        for lines in res:
            data.append(lines)

        return data

    def Extract(self):
        languages = {}
        table_name = 'Backend'
        data = self.show_data(table_name)
        for lines in data:
            languages[lines[0]] = lines[1:]

        return languages

    def Create_table(self,Table_name):
        try:
            self.cur.execute("CREATE TABLE {}(ID INT, NAME VARCHAR(20), SALARY INT, DEP VARCHAR(20))".format(Table_name))
        except:
            self.myconn.close()


    def Insert_data(self, tname):
        try:
            sql = "INSERT INTO {}(ID,NAME,SALARY,DEP) VALUES(%s,%s,%s,%s)".format(tname)
            val = (1, "Kalyan", 25000, "IT")
            self.cur.execute(sql,val)
            self.myconn.commit()

        except:
            self.myconn.rollback()



mydatabase = 'kalyan'
table_name = 'Backend'
obj = MY_DataBase()
# print(obj.Show_databases())
# print(obj.Connect_database(mydatabase))
# print(obj.Databases())
# print(obj.Table_data())

# print(obj.show_data(table_name))
#print(obj.Extract())

#------------------------------------------CREATE TABLE
# name = 'AMAZON'
# print(obj.Create_table(name))

#------------------------------------------INSERT DATA
tname = "TCS"
print(obj.Insert_data(tname))