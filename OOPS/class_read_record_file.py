class Match:
    def __init__(self, file_name):
 
        self.file_name = file_name
        self.females = {}
        self.males = {}
        for line in self.file_name:
            feilds = line.split()
            if 'f'==feilds[1]:
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

file_name = open("records.txt","r")

ob = Match(file_name)
ob.show()
