import sqlite3

class NotSuchEmployee(Exception):
        print("Not")

class Employee:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")


    def create_table(self):
        self.conn.execute('''create table if not exists records(empid text, name text, gender char(1),age text, salary text);''')


        
    def put(self,empid,name,gender,age,salary):
        self.conn.execute('''insert into records(empid,name,gender,age,salary) values(?,?,?,?,?)''',(empid,name,gender,age,salary))
        self.conn.commit()
    

    def delete(self,eid):
        cursor = self.conn.execute("select * from records")
        e = []
        for empid,name,gender,age,salary in cursor:
            e.append(empid)
        try:
            if eid in e:
                self.conn.execute('''DELETE FROM records where empid = '{}' '''.format(eid))
                self.conn.commit()   
        except NotSuchEmployee as err:
            raise NotSuchEmployee(err)

    def Show(self):
        cursor = self.conn.execute("select * from records")
        for empid,name,gender,age,salary in cursor:
            print(empid,name,gender,salary)



e1 = Employee()
e1.create_table()

#Add Employee-----------------------
#e1.put("E201","Ravi","m","24","25000")
#e1.put("E202","prasad","m","23","25020")
#e1.put("E203","kalyan","m","25","25200")

#Delete Employee--------------------

e1.delete('E202')
e1.Show()




