import os
import time
from Duplicate import *
from connection import *
from MailSender import *

def CreateLog(FolderName="Marvellous"):
    

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace("/","_")
    timestamp=timestamp.replace(":","_")
    FileName=os.path.join(FolderName,"Log.txt")
    Arr={}
    fd=open(FileName,'w')
    separator="-"*100

    fd.write(separator+"\n")
    fd.write(FileName+" Process Log"+"\n")
    fd.write("Log file created at :"+time.ctime()+"\n")
    fd.write(separator+"\n")
    Arr,cnt=FindDuplicate(FolderName)
    ArrList=PrintDuplicate(Arr)
    fd.write("CONTENTS OF LOG FILE "+"\n")
    fd.write(separator+"\n")
    for data in ArrList:
        fd.write("%s \n" %data)
    fd.write(separator+"\n")
   
    fd.close()
    delcount=DeleteFiles(Arr)
    connected=is_connected()
    
    if connected:
        startTime=time.time()
        
        MailSender(FileName,time.ctime(),cnt,delcount)
        endTime=time.time()

        print("Took %s seconds to send mail "%(endTime-startTime))
    else:
        print("There is no internet connection")