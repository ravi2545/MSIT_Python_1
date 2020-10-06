import re
class Elections:
    def __init__(self, file_names):
        self.file_names = file_names



    def Seats_Win_party(self):
        for name in self.file_names:
            f_obj = open(name, 'r')
            year = re.sub("[A-Za-z.]","",name)
            parties = {}
            count = 0
            for line in f_obj:
                feilds = line.split()
                party_name = feilds[4]
                if party_name in parties:
                    parties[party_name]+=count+1
                else:
                    parties[party_name]=count+1
            print(year)
            print(parties)


            
    def Highest_Margin(self):
        for name in self.file_names:
            f_obj = open(name, 'r')
            year = re.sub("[A-Za-z.]","",name)
            H_w_margin = []
            for line in f_obj:
                feilds = line.split()
                name = feilds[2]
                W_votes = int(feilds[5])
                L_votes = int(feilds[9])
                H_margin = W_votes-L_votes
                H_w_margin.append((H_margin, name))
            H_w_margin.sort()
            print(year)
            print(H_w_margin[-1])



    def Female_Winner(self):
        for name in self.file_names:
            f_obj = open(name, 'r')
            year = re.sub("[A-Za-z.]","",name)
            t_count = 0
            w_count = 0
            winners = {}
            for line in f_obj:
                feilds = line.split()
                w_female = feilds[3]
                l_female = feilds[7]
                if 'F' in w_female:
                    t_count+=1
                    w_count+=1
                if 'F' in l_female:
                    t_count+=1
                winners[year] = {"Total_females":t_count,"Winners":w_count}
            print(winners)
                    
        

file_names = ["Elections2004.txt", "Elections2009.txt", "Elections2014.txt"]
El = Elections(file_names)
El.Seats_Win_party()
El.Highest_Margin()
El.Female_Winner()
