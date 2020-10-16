class Player:
    def __init__(self):
        self.players = {}
        try:
            fobj = open('players.txt','r')
            for line in fobj:
                feilds = line.split()
                name = feilds[0]
                players = feilds[1:]
                for player in players:
                    self.addElement(name, player)
        except:
            pass
            
    def addElement(self, name, player):
        if name in self.players:
            if player not in self.players[name]:
                self.players[name].append(player)
        else:
            self.players[name] = [player]


    def remove1(self,name):
        if name in self.players:
            del self.players[name]

            
    def removefan(self, name, player):
        if name in self.players:
            if player in self.players[name]:
                self.players[name].remove(player)

    def save(self):
        fobj = open("players.txt","w")
        for line1 in self.players:
             fobj.write(line1+' ')
             for line in self.players[line1]:
                 fobj.write(line+' ')
             fobj.write("\n")

        fobj.close()


    def mostpopular_player(self):
        populars = {}
        final = []
        for name in self.players.values():
            for player in name:
                if player in populars:
                    populars[player]+=1
                else:
                    populars[player]=1
        for key, value in populars.items():
            final.append((value, key))

        final.sort()
        print(final[-1][-1])
            
    def show(self):
        for line1 in self.players:
             print(line1,end=" ")
             for line in self.players[line1]:
                 print(line,end=' ')
             print()


            
        

p1 = Player()
p1.addElement('ravi','prasad')
p1.addElement('ravi','vinod')

#p1.mostpopular_player()
p1.save()
p1.show()
