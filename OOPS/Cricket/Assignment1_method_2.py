import re
import statistics
class Cricket:
    def __init__(self, runs, balls):
        self.runs = runs
        self.balls = balls

    def strikes(self):
        strike=[]
        strike_rate = self.runs/self.balls*100
        strike.append(strike_rate)
        return strike



file_names = ["dravid.txt","sachin.txt"]
for name in file_names:
    f_obj = open(name, 'r')
    for line in f_obj:
        feilds = line.split()
        runs = int(feilds[2])
        balls = int(feilds[3])
        cr = Cricket(runs, balls)

r = cr.strikes()
for i in r:
    print(i)
