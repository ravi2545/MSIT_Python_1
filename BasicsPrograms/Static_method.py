# class Person:
#     ravi = 10
#     @classmethod
#     def Kalyan(cls):
#         print("kalyan Method")
#
#     @classmethod
#     def Prasad(cls):
#         print("Prasad")
#
#     # Static method knows nothing about the class and just deals with the parameters.
#     def Ravi():
#         return ("I am Ravi")
#
#
#
# Person.Ravi = staticmethod(Person.Ravi)
# print(Person.Ravi())
# print(Person.ravi)
#
#
# # Class method works with the class since its parameter is always the class itself.


class Person:
    name = "Kalyan"
    age = 23


    @staticmethod
    def show(name):
        print(name)

    def dis(cls):
       print("The Name and age is:", cls.name, cls.age)

Person.dis = classmethod(Person.dis)
Person.dis()

