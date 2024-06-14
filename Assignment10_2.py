import os
import sys

def FileChangeExt(Dir):
    count=0
    if os.path.exists(Dir):
        for folders,subfolders,files in os.walk(Dir):
            for fname in files:
                filepath=folders
                a=fname.split(".")
                if a[1]==sys.argv[2][1:]:
                    base=os.path.splitext(fname)[0]
                    file_path = os.path.join(filepath, fname)
                    new_name = os.path.join(filepath, base + sys.argv[3])
                    os.rename(file_path, new_name)
                    count=count+1
    else:
        print("Directory doesn't exists")

    if count==0:
        print("Directory does't exists file with ",sys.argv[2]," extension")


def main():
    if len(sys.argv)!=4:
        print("Invalid number of arguments ")
    else:

        try:
            FileChangeExt(sys.argv[1])
        except ValueError as vobj:
            print(vobj)
        except Exception as eobj:
            print(eobj)

    

if __name__=="__main__":
    main()