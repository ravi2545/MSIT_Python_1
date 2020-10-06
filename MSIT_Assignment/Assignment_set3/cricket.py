import statistics
file_obj = open('dravid.txt','r')
strike_rate = []
for line in file_obj:
    fields = line.split()
    runs = int(fields[2])
    balls = int(fields[3])
    strike_rates = runs/balls*100
    strike_rate.append(strike_rates)

print(strike_rate)
sd = statistics.stdev(strike_rate)
print(sd)
