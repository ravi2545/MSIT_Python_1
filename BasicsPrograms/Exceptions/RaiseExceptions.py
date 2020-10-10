# try:
#     a = [1,2]
#     n = 1
#     if n>len(a):
#         raise IndexError("Outof Range")
#     else:
#         print(a.index(n))
# except IndexError as d:
#     print(d)
# finally:
#     print("This is Division Operation")

#
# try:
#   a=2
#   b=0
#   if b==0:
#     raise ZeroDivisionError("Divi")
#   else:
#     print(a/b)
# except ZeroDivisionError as d:
#   print(d)
# finally:
#   print("result")



# try:
#     fileptr = open("file2.txt","r")
#     try:
#         fileptr.write("Hi I am good")
#     finally:
#         fileptr.close()
#         print("file closed")
# except:
#     print("Error")

# class Networkerror(RuntimeError):
#    def __init__(self, arg):
#       self.args = arg
#
# try:
#    raise Networkerror("Bad hostname")
# except Networkerror as e:
#    print(e.args)

# class MinimumSalary(Exception):
#     def __init__(self, n):
#         self.n = n
#
#     def __str__(self):
#         print("Minimum Salary nedd 20000 for aprove Loan Amount")
#
#
# n = 10000
# if not n>20000:
#     raise MinimumSalary(n)



# try:
#     a = 1
#     b = 0
#     if b==0:
#         raise ZeroDivisionError("Not divisible by zero")
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(a/b)
# finally:
#     print("Exceuted")



# class Ravi:
#     def __init__(self, name):
#         self.name = name
#
#     def __dir__(self):
#         return self.name
#
# name = "kalyan"
# ob = Ravi(name)
# print(dir(ob))

# try:
#     a = 10
#     b = 1
#     print(a/b)
# except:
#     print("Zero by division")
# else:
#     print(a/b)


f = open("records.txt","r")
try:
    f.write("I am Ravi")
except:
    f.close()
finally:
    print("kalyan")