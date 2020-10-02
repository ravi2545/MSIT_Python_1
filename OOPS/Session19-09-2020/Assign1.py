class Person:
    def __init__(self, name, gender, age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary

    def show(self):
        print(self.name, self.gender, self.age,self.salary)




f_obj = open("Session.txt", 'r')
person = []
for line in f_obj:
    feilds = line.split()
    name,gender,age,salary = feilds
    p1 = Person(name,gender,age,salary)
    person.append(p1)


for p in person:
    p.show()
    
