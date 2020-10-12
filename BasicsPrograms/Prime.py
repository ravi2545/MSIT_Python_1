# number = 0
# if number>1:
#     for i in range(2, number):
#         if (number%i) == 0:
#             print(number, "Is Not prime Number")
#             break
#     else:
#         print(number, "prime Number")
# else:
#     print(number, "Is not Prime")

prime = []
for num in range(2,100):
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        prime.append(num)


print(prime)
