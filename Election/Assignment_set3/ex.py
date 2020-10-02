import re
files = open("Elections2004.txt", "r")
year = re.sub("[A-Za-z.]","",files)
print(year)
