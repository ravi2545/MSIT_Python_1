class Basics:
    def __init__(self):
        self.temp = 1


    def fat(self, ls):
        for line in ls:
            self.temp = self.temp*line
        print(self.temp)


    def singNumber(self, sn):
        for line in range(1,sn+1):
            self.temp = self.temp*line
        print(self.temp)


    def swapping(self, sn, snl):
        sn, snl = snl, sn
        print(sn, snl)


    def simple_int(self, p, t, r):
        res = lambda p,t,r:p*t*r/100
        res(p,t,r)
        

sn = 5
sn1 = 34
r = 2
ls = [1,2,3,4,5]
ob = Basics()
#ob.fat(ls)
#ob.singNumber(sn)
#ob.swapping(sn, sn1)
ob.simple_int(sn,sn1,r)
