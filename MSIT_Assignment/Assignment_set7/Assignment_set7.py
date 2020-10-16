# class Employee(object):
#     def __init__(self, data):
#         super().__setattr__('data', dict())
#         self.data = data
#
#     def __getattr__(self, name):
#         if name in self.data:
#             return self.data[name]
#         else:
#             return 0
#
#     def __setattr__(self, key, value):
#         if key in self.data:
#             self.data[key] = value
#         else:
#             super().__setattr__(key, value)
#
#     def __bool__(self):
#         if self.data:
#             return True
#         else:
#             return False
#
#     def __eq__(self, other):
#         return "Not Equal"
#
#
# emp = Employee({'Ravi': "Kalyan"})
# p1 = Employee({"ravi","prasad"})
# emp.Ravi = "kalyan Laxmi"
# if p1:
#     print("True")
# else:
#     print("False")


class Player:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.players = {}

    def __bool__(self):
        if self.name and self.player:
            return True
        else:
            return False

    def __add__(self, other):
        if other:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False

    def __str__(self):
        return "Key is {} and Values {}".format(self.name,self.player)

    def __getattr__(self, item):
        print(item)


p1 = Player("Kalyan","Ravi")
p2 = Player("Kalyan","Ravi")
if p1:
    print("Added Item")
else:
    print("Not added")

print(p1==p2)
print(p1)