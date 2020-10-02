import subprocess

#p1 = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
#p2 = subprocess.Popen('mkdir empty',shell=True,stdout=subprocess.PIPE)
p1 = subprocess.Popen('python Session_28-09-2020.py -d " " ravi.txt',shell=True,stdout=subprocess.PIPE)
p2 = subprocess.Popen('python Session_28-09-2020.py -d " " -f 1,2',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
result = p2.stdout.read()
print(result.decode("utf-8"))

