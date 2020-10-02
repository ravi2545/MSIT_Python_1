import sqlite3
import xml.dom.minidom


class NotSuchEmployee(Exception):
    def __init__(self, eid):
        self.eid = eid

    def __str__(self):
        print("NoSuchEmployee-{}".format(self.eid))


class Employee:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")

    def create_table(self):
        self.conn.execute(
            '''create table if not exists records(empid text, name text, gender char(1),age text, salary text);''')

    def put(self, empid, name, gender, age, salary):
        self.conn.execute('''insert into records(empid,name,gender,age,salary) values(?,?,?,?,?)''',
                          (empid, name, gender, age, salary))
        self.conn.commit()

    def delete(self, eid):
        cursor = self.conn.execute("select * from records")
        employe_ids = []
        for empid, name, gender, age, salary in cursor:
            employe_ids.append(empid)
        if eid in employe_ids:
            self.conn.execute('''DELETE FROM records where empid = '{}' '''.format(eid))
            self.conn.commit()
            print("Delete employee ID {}".format(eid))
        else:
            raise NotSuchEmployee(eid)

    def Modify(self, emid, name, gender, age, salary):
        cursor = self.conn.cursor()
        d = cursor.execute("select * from records")
        emplid = []
        for e in d:
            emplid.append(e[0])
        if emid in emplid:
            sql_update_query = """Update records set salary = ?, name = ?, gender = ?, age = ?, salary = ? where empid = ?"""
            data = (salary, name, gender, age, salary, emid)
            cursor.execute(sql_update_query, data)
            self.conn.commit()
            print("Record Updated successfully")
            cursor.close()
        else:
            raise NotSuchEmployee(emid)


    def get(self,eid):
        cursor = self.conn.execute("select * from records")
        ids = []
        details = []
        for empid,name,gender,age,salary in cursor:
            ids.append(empid)
            details.append((empid,name,gender,age,salary))
        if eid in ids:
            for d in details:
                if eid in d:
                  pass


        else:
            raise NotSuchEmployee(eid)


    def Show(self):
        cursor = self.conn.execute("select * from records")
        for empid, name, gender, age, salary in cursor:
            print(empid, name, gender, salary)


e1 = Employee()
e1.create_table()

# Add Employee------------------------------------
# e1.put("E201","Ravi","m","24","25000")
# e1.put("E202","prasad","m","23","25020")
# e1.put("E203","kalyan","m","25","25200")

# Delete Employee--------------------------------

# e1.delete('E203')

# Modify------------------------------------------

#e1.Modify('E201', 'Govinda', 'f', '21', '33000')

# ------------------ Getting Data in XML format

e1.get('E201')
e1.Show()
