def mean(x):
    return sum(x)/len(x)



def median(x):
    x.sort()
    if len(x)%2==0:
        t = int(len(x)/2)
        temp1 = x[t]
        temp2 = x[t-1]
        dif = (temp1+temp2)/2
        return dif
    else:
        t = int(len(x)/2)
        temp1 = x[t]
        return temp1



def mode(x):
    e= {}
    for i in x:
        if i in e:
            e[i]+=1
        else:
            e[i]=1

    final = []
    for element,repeats in e.items():
        final.append((repeats, element))
    final.sort()
    return final[-1][-1]
