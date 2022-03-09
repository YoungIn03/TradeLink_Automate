import os
import xml.etree.ElementTree as ET
import os

# get customer PO from text file 
# delete empty lines 
text_file = open("C:/Users/youngin.kim/Desktop/Tradelink/Value search Program/datafiles/poList.txt", "r")
cust_PO = text_file.read().splitlines() 
text_file.close()
cust_PO = ' '.join(cust_PO).split()
print(cust_PO)

#create empty list to store POs for later
file_PO = []
received_PO = []
not_received_PO = []

rootdir = "C:/Users/youngin.kim/Desktop/Tradelink/Value search Program/EDI/03"
#rootdir = "://192.168.11.3/ftp/CTRC/ARCHIVE/940/2022/03/"

# go through all files in subfolders 
for subdir, dirs, files in os.walk(rootdir): 
    for filename in files:
        if filename.endswith(".xml"): 
            tree = ET.parse(subdir + "/" + filename)
            root = tree.getroot()

            # check the PO number for all the xml files in subfolder
            # append PO# that has not been appended already to file_PO list
            for ordernum in root.iter('ORDERNUM'): 
                PO = (ordernum.text)
                if PO in file_PO: 
                    continue
                else: 
                    file_PO.append(PO) 
                    
                    

# if cust_PO exists in file_PO, append the PO to received PO list 
# print received PO list 
for i in cust_PO: 
    if i in file_PO: 
        received_PO.append(i)
    else: 
        not_received_PO.append(i)

if len(not_received_PO) == 0: 
    print("All POs Received") 
else: 
    print('\nMissing\n', *not_received_PO, sep='\n ')
    print('\nReceived\n',*received_PO, sep ='\n ')


print(rootdir)