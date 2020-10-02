import re
import statistics as sd
import openpyxl
class Cricket:
    def __init__(self, filenames):
        self.filenames = filenames
        for name in self.filenames:
            fobj = open(name,'r')
            #self.Standard_dev(fobj, name)
            self.Create_excel_file(name, fobj)




    def Standard_dev(self, fobj, name):
        strike_rates = []
        player = re.sub("[.txt]","",name)
        players_list = {}
        for line in fobj:
            feilds = line.split()
            runs = int(feilds[2])
            balls = int(feilds[3])
            strike_rate = runs/balls*100
            strike_rates.append(strike_rate)
        sdv = sd.stdev(strike_rates)
        players_list[player] = sdv
        print(players_list)




    def Create_excel_file(self, name, fobj):
        player = re.sub("[.txt]","",name)
        wb = openpyxl.Workbook()
        sheet = wb["Sheet"]
        wb.remove(sheet)
        sheet = wb.create_sheet(name)
        for line,data in enumerate(fobj):
            feilds = data.split()
            sheet.append(feilds)
            
        wb.save("excel_cricket_data.xlsx")


        

filenames = ["dravid.txt","sachin.txt","virat.txt","yuvraj.txt"]
ob = Cricket(filenames)

