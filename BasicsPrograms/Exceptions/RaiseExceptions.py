# try:
#     a = 1
#     b = 0
#     if b==0:
#         raise ZeroDivisionError("Denominator does not contains zero Value")
#     else:
#         print(a/b)
# except ZeroDivisionError as d:
#     print(d)
# finally:
#     print("This is Division Operation")

#
# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#   f.close()


# try:
#     fileptr = open("file2.txt","r")
#     try:
#         fileptr.write("Hi I am good")
#     finally:
#         fileptr.close()
#         print("file closed")
# except:
#     print("Error")

class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print(e.args)