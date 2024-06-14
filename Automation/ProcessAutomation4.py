import psutil
import time
import schedule
import os
import datetime
import sys

def CreateLog(FolderName="Marvellous"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName=os.path.join(FolderName,"Marvellous%s.log" %(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')))

    fd=open(FileName,'w')
    separator="-"*100

    fd.write(separator+"\n")
    fd.write(FileName+" Process Log"+"\n")
    fd.write("Log file created at :"+time.ctime()+"\n")
    fd.write(separator+"\n")
    Arr=GetProcessInfo()
    fd.write("CONTENTS OF LOG FILE "+"\n")
    fd.write(separator+"\n")
    for data in Arr:
        fd.write("%s \n" %data)
    fd.write(separator+"\n")
   
    fd.close()


def GetProcessInfo():
    listprocess=[]
    for proc in psutil.process_iter(['pid','name','username']):
        listprocess.append(proc.info)
    
    return listprocess

    
def main():
    schedule.every(int(sys.argv[1])).minutes.do(CreateLog)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
  
if __name__=="__main__":
    main()