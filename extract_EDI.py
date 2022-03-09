import xml.etree.ElementTree as ET
import os
import shutil


rootdir = "C:/Users/youngin.kim/Desktop/Tradelink/Value search Program/EDI/02/"
destination_folder = "C:/Users/youngin.kim/Desktop/Tradelink/Value search Program/Extracted/"


purchaseOrder = []
edi_filename = []


# cust_PO = ['31312354', '31312356', '31312358', '31353668', '31353669', '31353672', '31353673', '31353674', 
#             '31353675', '31486075', '8636524K', '8654790K', '8654816K', '8654824K', '8660227K', '8660235K', '8660300K', 
#             '8660318K', '8711988K', '8712036K', '8712044K', '8723389K', '8723397K', '8723868K', '8723876K', '8723884K', 
#             '8744534K', '9549148C', '9562570C', '9562596C', '9562604C', '9612250C', '9612300C', '9612318C', '9625161C', 
#             '9625179C', '9625633C', '9625641C', '9625658C', '9645318C', '9667684R', '9683053R', '9683079R', '9683087R', 
#             '9738741R', '9738790R', '9738808R', '9753641R', '9753658R', '9754128R', '9754136R', '9754144R', '9770926R', 
#             '31312324', '31312325', '31312326', '31312327', '31312328', '31312329', '8636474K', '8636490K', '9549098C', 
#             '9549114C', '9667635R', '9667650R', '8671810K', '9576604C', '9703893R', '9683129R', '9562646C', '8654873K', 
#             '31353684', '9549122C', '8636508K', '9667668R', '8636466K', '9667627R', '9549080C', '9754110R', '9625625C', 
#             '8723850K', '9753625R', '9625146C', '8723363K', '9753617R', '9625138C', '8723355K', '9753609R', '9753740R', 
#             '9625252C', '8723488K', '9753732R', '8723470K', '9753724R', '9625245C', '8723462K', '9754102R', '9625617C', 
#             '8723843K', '9625120C', '8723348K']
            
cust_PO=['8711988K', '8712036K', '8712044K', '9612250C', '9612300C', '9612318C', '9738741R', '9738790R', '9738808R']
iter = 0 

#go through all files in subfolders 
for subdir, dirs, files in os.walk(rootdir):
    for filename in files: 
        if filename.endswith("xml"): 
            tree = ET.parse(subdir + "/" + filename) 
            root = tree.getroot()

        
            #append all the file names that has matching PO numbers in cust_PO
            #if the corresponding PO exists, remove the PO# from the original list 
            for ordernum in root.iter('ORDERNUM'):
                PO = (ordernum.text) 
                if PO in cust_PO: 
                    edi_filename.append((filename.rsplit('.',1)[0])+'.edi')
                    cust_PO.remove(PO)
                    #move the edi files 
                    shutil.copy2(subdir + "/" + edi_filename[iter], destination_folder)
                else: 
                    continue
                iter += 1

print('\nextracted files\n', *edi_filename, sep='\n ')
print('\nmissing POs\n', *cust_PO, sep='\n ')



#for filename in os.listdir(source_folder): 
#    if filename.endswith(".xml"): 
#        tree = ET.parse(filename)
#        root = tree.getroot()
# if PO in purchaseOrder:
#     continue
# else: 
#     purchaseOrder.append(PO)



