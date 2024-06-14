import sys
import os
from shutil import copyfile

def DirectoryCopy(Dir):
    if os.path.exists(Dir):
        os.mkdir(sys.argv[2])
        temp_path=os.path.abspath(sys.argv[2])
        for folders, subfolders,files in os.walk(Dir):
            for fname in files:
                file_path=folders
                src=os.path.join(file_path,fname)
                dec=os.path.join(temp_path,fname)
                copyfile(src,dec)
    else:
        print("Directory dosen't exists")



def main():
   if len(sys.argv)!=3:
        print("Invalid number of arguments ")
   else:
        try:
            DirectoryCopy(sys.argv[1])
        except ValueError as vobj:
            print(vobj)
        except Exception as eobj:
            print(eobj)

if __name__=="__main__":
    main()
