class NotAString(Exception):
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return "Not a string element in append {}".format(self.element)


class StringList(list):
    def append(self, element):
        if type(element) == str:
            list.append(self, element)
        else:
            raise NotAString(element)
            

s1 = StringList()

s1.append("python")
s1.insert(0,"ruby")
s1.append("pandas")

print(s1)
s1.sort()
print(s1)
s1.append(75)
print(s1)

