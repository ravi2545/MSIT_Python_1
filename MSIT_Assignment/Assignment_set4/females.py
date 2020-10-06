import re
files = ["Elections2004.txt", "Elections2009.txt", "Elections2014.txt"]

for file_name in files:
    year = re.sub("[A-Za-z.]","",file_name)
    f_obj = open(file_name, 'r')
    winners = {}
    Total_females_count = 0
    Winner_female_count = 0
    for data in f_obj:
        feilds = data.split()
        wGn = feilds[3]
        lGn = feilds[7]
        if 'F' in wGn:
            Total_females_count+=1
            Winner_female_count+=1
            
        if 'F' in lGn:
            Total_females_count+=1
    winners[year] = {"Total_females":Total_females_count, "Winner_females":Winner_female_count}
    print(winners)
