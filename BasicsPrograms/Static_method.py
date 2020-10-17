class Person:
    @classmethod
    def Kalyan(cls):
        print("kalyan Method")

    @classmethod
    def Prasad(cls):
        print("Prasad")

    # Static method knows nothing about the class and just deals with the parameters.
    def Ravi():
        return ("I am Ravi")


Person.Ravi = staticmethod(Person.Ravi)
print(Person.Ravi())


# Class method works with the class since its parameter is always the class itself.
