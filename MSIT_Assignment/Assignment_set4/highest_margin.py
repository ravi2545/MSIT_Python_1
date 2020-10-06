import re
file_names = ["Elections2004.txt", "Elections2009.txt", "Elections2014.txt"]
w = {}

for name in file_names:
    f_obj = open(name, 'r')
    year = re.sub("[A-Za-z.]", "", name)
    ww = []
    for line in f_obj:
        feilds = line.split()
        wvotes = int(feilds[5])
        lvotes = int(feilds[9])
        names = feilds[2]
        hwin = wvotes-lvotes
        ww.append((hwin, names))
    ww.sort()
    w[year]=ww[-1][-1]
    
print(w)
