try:
    a = 1
    b = 1
    if b==0:
        raise ZeroDivisionError("Not divisible by zero")
except ZeroDivisionError as e:
    print(e)
else:
    print(a/b)