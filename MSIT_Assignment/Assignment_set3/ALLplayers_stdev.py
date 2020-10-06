import statistics
import re

file_names = ['dravid.txt', 'sachin.txt', 'virat.txt', 'yuvraj.txt']
players = {}

for names in file_names:
    strike_rates=[]
    f_obj = open(names, 'r')
    player = re.sub(".txt","",names)
    for line in f_obj:
        feilds = line.split()
        runs = int(feilds[2])
        balls = int(feilds[3])
        strike_rate = runs/balls*100
        strike_rates.append(strike_rate)
    sd = statistics.stdev(strike_rates)
    players[player]=sd
        

print(players)
        
