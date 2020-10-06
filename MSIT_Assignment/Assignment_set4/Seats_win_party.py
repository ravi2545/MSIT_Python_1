import re
file_names = ["Elections2004.txt", "Elections2009.txt", "Elections2014.txt"]
parties = {}
count = 0
for line in file_names:
    f_obj = open(line, 'r')
    year = re.sub("[A-Za-z.]","",line)
    print(year)
    for data in f_obj:
        feilds = data.split()
        name = feilds[4]
        votes = feilds[5]
        if name in parties:
            parties[name]+=count+1
        else:
            parties[name]=count+1
    print(parties)
  
