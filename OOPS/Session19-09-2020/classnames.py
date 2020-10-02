class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def show(self):
        print(self.name)
        print(self.gender)
        print(self.age)


class Employee(Person):
    def __init__(self, name, gender, age, salary):
        Person.__init__(self, name, gender, age)
        self.salary = salary


    def show(self):
        Person.show(self)
        print(self.salary)


e1 = Employee("Allen", "m", 38, 75000)
e1.show()
