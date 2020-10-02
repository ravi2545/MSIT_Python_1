import sqlite3

conn = sqlite3.connect("database.db")

conn.execute('''create table if not exists records(id integer primary key autoincrement, name text, gender char(1),age text, salary text);''')

fobj = open('records.txt','r')

for line in fobj:
    feilds = line.split()
    name,gender,age,salary = feilds

    conn.execute('''insert into records(name,gender,age,salary) values(?,?,?,?)''',(name,gender,age,salary))

conn.commit()

cursor = conn.execute("select * from records")

for id,name,gender,age,salary in cursor:
    print(id,name,gender,salary)



def post():
    pass

