import math


class Match:
    def __init__(self):
 
        self.file_name = open("records.txt","r")
        self.females = {}
        self.males = {}
        self.empty=[]
        for line in self.file_name:
            feilds = line.split()
            name = feilds[0]
            gender = feilds[1]
            age = feilds[2]
            salary = int(feilds[3])
            self.empty.append(salary)
            if gender=="f":
                self.females[feilds[0]] = {"age":feilds[2],"salary":feilds[3]}
            else:
                self.males[feilds[0]]= {"age":feilds[2],"salary":feilds[3]}

        
    def show(self):
        print("Printing all the male records...")
        for name in self.males:
            print(name,end=" ")
            print(self.males[name]["age"],end=" ")
            print(self.males[name]["salary"])
        print()
        print("Printing all the male records...")
        for name in self.females:
            print(name,end=" ")
            print(self.females[name]["age"],end=" ")
            print(self.females[name]["salary"])
        print()




    def Distance(self,male,female):
        mage = int(self.males[male]["age"])
        fage = int(self.females[female]["age"])
        m_normalize = int(self.males[male]["Normalize"])
        f_normalize = int(self.females[female]["Normalize"])
        adif = math.sqrt((mage-fage)**2 + (m_normalize-f_normalize)**2)
        return adif




    def recommendFemale(self,male):
        recommend = []
        for name in self.females:
            result = self.Distance(male,name)
            recommend.append((result,male,name))
        recommend.sort()
        return (recommend[0][2])



    def Normalize(self):
        max_sa = max(self.empty)
        min_sa = min(self.empty)
        me_range = max_sa-min_sa
        for name in self.males:
            sal = int(self.males[name]["salary"])
            avg = ((sal - min_sa)/me_range)
            self.males[name]["Normalize"]=avg

        for name in self.females:
            fsal = int(self.females[name]["salary"])
            avg = ((fsal-min_sa)/me_range)
            self.females[name]["Normalize"]=avg




ob = Match()
ob.Normalize()
#ob.show()
print(ob.Distance("murali","geetha"))
#ob.Distance("murali","rani")
#ob.Distance("murali","mary")

print(ob.recommendFemale("murali"))

