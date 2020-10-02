import sys


args = sys.argv[1:]


p = int(args[0])
r = int(args[1])
t = int(args[2])

print("Principal={}, rate={}, time={}".format(p,r,t))
print()
print(p*t*r/100)

