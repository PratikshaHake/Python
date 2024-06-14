import sys
import os
from shutil import copyfile

def DirectoryCopyExt(Dir):
    count=0
    if os.path.exists(Dir):
        os.mkdir(sys.argv[2])
       
        temppath = os.path.abspath(sys.argv[2])
        for folders, subfolders,files in os.walk(Dir):
            for file in files:
                s=file.split(".")
                if s[1] == sys.argv[3][1:]:
                        filepath = folders
                        src = os.path.join(filepath, file)
                        dst = os.path.join(temppath, file)
                        copyfile(src, dst)
                        count=count+1
        if count==0:
            print(sys.argv[1]," directory dosen't contains file with ",sys.argv[3]," extension")

    else:
        print("Directory dosen't exists")

   

def main():
    if len(sys.argv[1])!=4:
        print("Invalid number of arguments ")
    else:
        try:
            DirectoryCopyExt(sys.argv[1])
        except ValueError as vobj:
            print(vobj)
        except Exception as eobj:
            print(eobj)

    

if __name__=="__main__":
    main()