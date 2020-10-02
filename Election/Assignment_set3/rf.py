l = [1,2,3,[1,2,3],[1,2]]
e = []
def rem(l):
    for i in l:
        if type(i) == list:
            rem(i)
        else:
            e.append(i)


rem(l)
print(e)
