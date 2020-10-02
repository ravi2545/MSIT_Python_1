import re
import openpyxl
wb = openpyxl.Workbook()
sheet = wb["Sheet"]
wb.remove(sheet)
file_name = ["dravid.txt","sachin.txt","yuvraj.txt","virat.txt"]

for names in file_name:
    name = re.sub("[.txt]","",names)
    sheet = wb.create_sheet(name)
    fobj = open(names, 'r')
    for line in fobj:
        feilds = line.split()
        sheet.append(feilds)

wb.save("ravi.xlsx")

