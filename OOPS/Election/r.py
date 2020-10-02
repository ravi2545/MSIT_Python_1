import re
class Elections:
    def __init__(self, f_obj, year):
        self.f_obj = f_obj
        self.year = year



    def Seats_Win_party(self):
        parties = {}
        for line in self.f_obj:
            feilds = line.split()
            party_name = feilds[4]
            if party_name in parties:
                parties[party_name]+=1
            else:
                parties[party_name]=+1
        print(self.year)
        print(parties)


    def H_margin(self):
        H_w_margin = []
        for line in self.f_obj:
            feilds = line.split()
            name = feilds[2]
            W_votes = int(feilds[5])
            L_votes = int(feilds[9])
            H_margin = W_votes-L_votes
            H_w_margin.append((H_margin, name))
        H_w_margin.sort()
        ww = H_w_margin[-1][-1]
        print(self.year)
        print(ww)
                    
        

file_names = ["Elections2004.txt", "Elections2009.txt", "Elections2014.txt"]
s = []
for names in file_names:
    year = re.sub("[A-Za-z.]","",names)
    f_obj = open(names,"r")
    El = Elections(f_obj, year)
    s.append(El)
        


for j in s:
    j.H_margin()
