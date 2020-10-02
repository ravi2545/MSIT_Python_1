import re
import statistics
class Cricket:
    def __init__(self,file_names):
        self.file_names = file_names


    def Sdeviation(self):
        player = {}
        for names in self.file_names:
            name = re.sub("[.txt]","",names)
            f_obj = open(names, 'r')
            strike_rates = []
            for line in f_obj:
                feilds = line.split()
                runs = int(feilds[2])
                balls = int(feilds[3])
                srike_rate = runs/balls*100
                strike_rates.append(srike_rate)
            sd = statistics.stdev(strike_rates)
            player[name] = sd
        print(player)


file_names = ["dravid.txt","sachin.txt","virat.txt","yuvraj.txt"]
player = {}
cr = Cricket(file_names)
cr.Sdeviation()
    
