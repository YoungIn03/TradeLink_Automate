text_file = open("C:/Users/youngin.kim/Desktop/Tradelink/Value search Program/datafiles/poList.txt", "r")
cust_PO = text_file.read().splitlines()
print(cust_PO)
text_file.close()

