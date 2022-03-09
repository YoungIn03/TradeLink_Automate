from openpyxl import load_workbook
from xml.dom import minidom 
import xml.etree.ElementTree as ET 


#excel file location 
read_xlsx = load_workbook(r'C:\Users\youngin.kim\Desktop\Tradelink\Value search Program\SP22 NPG SO-PO List 3.2.22.xlsx')

#read PO values in excel and store them into a list 
read_sheet = read_xlsx.active

name_col = read_sheet['F']
names = []

for cell in name_col:
    names.append(cell.value)

cust_PO = list(dict.fromkeys(names))

print(cust_PO)



