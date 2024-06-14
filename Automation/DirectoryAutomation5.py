import sys
import os
import time

def DirectoryWatcher(DirName,FileName):
    Count=0
    
    flag=os.path.isabs(DirName)
    if flag==False:
        print("Path is not absolute path")
        DirName=os.path.abspath(DirName)
        print("Converted absolute path is: ",DirName)

    exist=os.path.isdir(DirName)
    if (exist==True):
        for foldername,subfoldername,filename in os.walk(DirName):
            for name in filename:
               if(name==FileName):
                   print("File is present in the directory")
                   break
               
    else:
        print("There is no such directory")


def main():
    print("----------------------------------------")
    print("-----Directory Watcher-----")
    print("----------------------------------------")

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to perform directory traversal")
            exit()

        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage of the script : ")
            print("Name_Of_Application Name_Of_Directory Name_of_File")
            print("Note: Both the arguments should be in the integral format")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to get the help and use --u option to get the usage of application")
            exit()
            
    if(len(sys.argv)==3):
        try:
            starttime=time.time()
            DirectoryWatcher(sys.argv[1],sys.argv[2])
            endtime=time.time()

            print("Time required for the execution is :",endtime-starttime)
        
      
        except Exception as obj2:
            print("Unable to perform the task due to ",obj2)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()
    
    print("----------------------------------------")
    print("-----Thank you for using our script-----")
    print("-----------------Pratiksha--------------")



if __name__=="__main__":
    main()