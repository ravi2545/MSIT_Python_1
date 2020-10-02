import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-p",type=int, dest = 'principal', required=True)
parser.add_argument("-r",type=int, dest = 'rate', default=2)
parser.add_argument("-t",type=int, dest = 'time', default=12)
#parser.add_argument('city',nargs='?') 0 or 1
#parser.add_argument('city',nargs='*') 0 or more

parser.add_argument('city',nargs='+') #1 or more



args = parser.parse_args()
city = args.city



args = parser.parse_args()
p = args.principal
r = args.rate
t = args.time

print("Principal is {}, rate is {} and time is {}".format(p,r,t))


