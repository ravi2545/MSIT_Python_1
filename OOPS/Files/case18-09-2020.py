import re
class Poem:
    def __init__(self):
        self.lines = []
        fobj = open("poem.txt",'r')

        for line in fobj:
            self.lines.append(line)


            
    def show(self):
        for data in self.lines:
            print(data.strip())
        print()



    def clean(self):
        pat ='[^A-Za-z0-9 ]'
        
        for index,line in enumerate(self.lines):
            self.lines[index] = re.sub(pat,"",line)



    def clean1(self):
        pat ='[^A-Za-z0-9 ]'
        self.lines = list(map(lambda line:re.sub(pat,"",line),self.lines))



    def clean2(self):
        pat ='[^A-Za-z0-9 ]'
        self.lines = [re.sub(pat,"",line) for line in self.lines]



    def word_count(self):
        word_c = {}
        e = []
        for line in range(len(self.lines)):
            sp = self.lines[line].split()
            for l in sp:
                e.append(l)
        for data in e:
            if data in word_c:
                word_c[data]+=1
            else:
                word_c[data]=1

        print(word_c)



    def Word_count1(self):
        word_count = {}
        for line in self.lines:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1
        print(word_count)




    def getAllTheLines_2(self, word):
        result = [word]
        for line_number, line in enumerate(self.lines):
            if word in line:
                result.append((line_number+1, line))
        print(result)



    def getAllTheLies_3(self, word):
        result = [(line_number+1,line) for line_number, line in enumerate(self.lines) if word in line]
        result.insert(0,word)
        print(result)
        
                       
        
p1 = Poem()
p1.clean1()
p1.getAllTheLines("land")
p1.getAllTheLines_2("land")

