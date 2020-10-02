import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("-d",type=str, dest = 'delim', required=True)
parser.add_argument("-f",type=str, dest = 'feilds', default="all")

#parser.add_argument('city',nargs='?') 0 or 1
#parser.add_argument('city',nargs='*') 0 or more

parser.add_argument('filename',nargs='?') #0 or 1

args = parser.parse_args()

delim = args.delim
feilds = args.feilds
filename = args.filename

#print("delim = {}, f= {}, filename = {}".format(d,f,filename))

if filename:
    fobj = open(filename,"r")
else:
    import sys
    fobj = sys.stdin.readlines()


def isValid(feilds):
    pat = '^\d+(,\d+)*$'

    if re.match(pat, feilds):
        return True
    return False


def validIndexes(components, feilds):
    indexes = []
    feilds = feilds.split(",")
    for field in feilds:
        if int(field) > 0 and int(field) <= len(components):
            indexes.append(int(field)-1)
    indexes.sort()
    return indexes


if isValid(feilds):
    for line in fobj:
        components = line.strip().split(delim)
        indexes = validIndexes(components, feilds)
        for index in indexes:
            print(components[index], end=" ")
        print()
else:
    for line in fobj:
        print(line)


