file_obj = open("Players.txt",'r')
players = {}
for line in file_obj:
    fields = line.split()
    player = fields[0]
    fans = int(fields[1])
    if player not in players:
        players[player] = fans
    else:
        players[player] += fans
    

print(players)


    
    
