import re
class Elections:
    def __init__(self, files):
        self.files = files
        for file_name in files:
            fobj = open(file_name,"r")
            for line in fobj:
                feilds = line.split()
                self.show(feilds)


    def show(self, feilds):
        parties= {}
        for names in files:
            self.name = re.sub("[A-za-z.]","",names)
            party = feilds[4]
            if party in parties:
                parties[party]+=1
            else:
                parties[party]=1

        print(self.name, parties)






files = ["Elections2004.txt","Elections2009.txt","Elections2014.txt"]
ob_ject = Elections(files)
