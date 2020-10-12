class Person:
    def __init__(self, aadhar, name, gender, age):
        self.aadhar = aadhar
        self.name = name
        self.gender = gender
        self.age = age

    def __bool__(self):
        if self.age < 20:
            return False
        else:
            return True

    def __eq__(self, obj):
        if self.aadhar == obj.aadhar:
            return True
        else:
            return False

    def __str__(self):
        return "Hello"

    def show(self):
        print(self.name, self.gender, self.age)


p1 = Person("E001","gary", "m", 22)
p2 = Person("E002","jane", "f", 23)


if p1:
    print("NOT")
else:
    print("Ravi")

if p1==p2:
    print("equal")
else:
    print("Not Equal")