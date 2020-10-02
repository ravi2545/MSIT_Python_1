d = {'raj':['steve','sachin'], 'ravi':['dravid', 'sachin']}
count=0
e = {}
for k,l in d.items():
    for j in l:
        if j in e:
            e[j]+=count+1
        else:
            e[j]=count+1
print(e)
