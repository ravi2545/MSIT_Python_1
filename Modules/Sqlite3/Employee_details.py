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
        self.conn.execute(
            '''create table if not exists records(empid text, name text, gender char(1),age text, salary text);''')
        self.cur = self.conn.execute("select * from records")
        # rows=self.cur.fetchall()
        self.e = []
        self.data = []
        for r in self.cur:
            self.e.append(r[0])
            self.data.append((r[0], r[1], r[2], r[3], r[4]))

    def put(self, empid, name, gender, age, salary):
        if empid not in self.e:
            self.conn.execute('''insert into records(empid,name,gender,age,salary) values(?,?,?,?,?)''',
                              (empid, name, gender, age, salary))
            self.conn.commit()
        else:
            raise NotSuchEmployee(empid)

    def delete(self, eid):
        if eid in self.e:
            self.conn.execute('''DELETE FROM records where empid = '{}' '''.format(eid))
            self.conn.commit()
            print("Delete employee ID {}".format(eid))
        else:
            raise NotSuchEmployee(eid)

    def Modify(self, emid, name, gender, age, salary):
        if emid in self.e:
            sql_update_query = """Update records set salary = ?, name = ?, gender = ?, age = ?, salary = ? where empid = ?"""
            data = (salary, name, gender, age, salary, emid)
            self.conn.execute(sql_update_query, data)
            self.conn.commit()
            print("Record Updated successfully")
            self.conn.close()
        else:
            raise NotSuchEmployee(emid)

    def get(self, eid):
        if eid in self.e:
            for d in self.data:
                if eid in d:
                    l = ["Name","Gender","Age","Salary"]
                    doc = xml.dom.minidom.Document()
                    Employees = doc.createElement("Employees")
                    i = 1
                    for line in l:
                        line = doc.createElement(line)
                        text = doc.createTextNode(d[i])
                        line.appendChild(text)
                        Employees.appendChild(line)
                        i+=1
                    doc.appendChild(Employees)
                    print(doc.toprettyxml())

        else:
            raise NotSuchEmployee(eid)

    def Show(self):
        cursor = self.conn.execute("select * from records")
        for empid, name, gender, age, salary in cursor:
            print(empid, name, gender, salary)


e1 = Employee()

# Add Employee------------------------------------
# e1.put('E201', 'Ravi', 'm', '24', '25000')
# e1.put("E202","prasad","m","23","25020")
# e1.put("E203","kalyan","m","25","25200")

# Delete Employee--------------------------------

# e1.delete('E201')

# Modify------------------------------------------

# e1.Modify('E201', 'Govinda', 'f', '21', '33000')

# ------------------ Getting Data in XML format

e1.get('E201')
# e1.Show()
