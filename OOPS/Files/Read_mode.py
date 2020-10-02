class Player:
    def __inti__(self):
        self.players = {}

    def addElement(self, name, player):
        if name in self.players:
            self.players[name].append(player)
        else:
            self.players[name] = [player]

p1 = Player()
p1.addElement('chirag','steve')
