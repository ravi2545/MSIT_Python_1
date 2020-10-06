s = "Monika"
name = []
for line in s:
    name.append(line)
print(name)
name[2]='i'
name[3]='n'
print(name)
oupt = ""
for data in name:
    oupt+=data

print(oupt)