import sqlite3
class Employee:

    def __init__(self):

        self.conn = sqlite3.connect("databasess.db")
        self.conn.execute(
            "create table if not exists records(id text primary key unique ,name text,gender char(1),age INTEGER,salary INTEGER);")
        cur = self.conn.cursor()
        cur.execute("select * from records")
        self.rows = cur.fetchall()
        self.ids = []
        self.empid = []
        for row in self.rows:
            self.ids.append(row)
        for num in self.ids:
            self.empid.append(num[0])
        self.conn.commit()

    def addEmployee(self, id, name, gender, age, salary):

        if id not in self.empid:
            self.conn.execute("insert into records(id,name,gender,age,salary) values(?,?,?,?,?)",
                              (id, name, gender, age, salary))
            self.conn.commit()
            print("{} - {} - Employee add to Database".format(id, name))
            print()
        else:
            raise Exception('{} EmployeeAlreadyExists'.format(id))

    def deleteEmployee(self, id):

        if id in self.empid:
            self.conn.execute("delete from records where id =?", (id,))
            self.conn.commit()
            print("{} Employee Deleted from Database".format(id))
            print()
        else:
            raise Exception('NoSuchEmployee - {}'.format(id))

    def modifyEmployee(self, id, name, gender, age, salary):

        if id in self.empid:
            self.conn.execute("update records set name=?,gender=?,age=?,salary=? where id = ?",
                              (name, gender, age, salary, id))
            self.conn.commit()
            print("{} - {} Employee Modifed".format(id, name))
            print()
        else:
            raise Exception('NoSuchEmployee - {}'.format(id))

    def dataInXml(self, id):

        cur = self.conn.cursor()
        cur.execute("select * from records where id=?", (id,))
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append(row)
        for emp in data:
            names, genders, ages, salarys = emp[1], emp[2], str(emp[3]), str(emp[4])

            import xml.dom.minidom
            doc = xml.dom.minidom.Document()

            main = doc.createElement('Employee')
            doc.appendChild(main)

            name = doc.createElement('name')
            nameText = doc.createTextNode(names)
            name.appendChild(nameText)
            main.appendChild(name)

            gender = doc.createElement('gender')
            genderText = doc.createTextNode(genders)
            gender.appendChild(genderText)
            main.appendChild(gender)

            age = doc.createElement('age')
            ageText = doc.createTextNode(ages)
            age.appendChild(ageText)
            main.appendChild(age)

            salary = doc.createElement('salary')
            salaryText = doc.createTextNode(salarys)
            salary.appendChild(salaryText)
            main.appendChild(salary)

            print(doc.toprettyxml())

    def show(self):

        data = []
        for row in self.rows:
            data.append(row)
        print("-----Existing Employees-----")
        for emp in data:
            id, name, gender, age, salary = emp[0], emp[1], emp[2], str(emp[3]), str(emp[4])
            print(id, name, gender, age, salary)


e1 = Employee()
e1.addEmployee("E007","Akhil","m",24,65000)
# e1.deleteEmployee("E004")
# e1.modifyEmployee("E005","divya","m",22,15000)
# e1.dataInXml("E001")
e1.show()