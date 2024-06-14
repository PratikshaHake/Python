import os
import sys

def FileSearch(Dir):
    count=0
    if os.path.exists(Dir):
        for folders,subfolders,files in os.walk(Dir):
            for fname in files:
                if fname.endswith(sys.argv[2]):
                    print(fname)
                    count=count+1

                    
    else:
        print("Directory doesn't exists")
        exit()

    if count==0:
        print("Directory does't exists file with ",sys.argv[2]," extension")


def main():

    if len(sys.argv)!=3:
        print("Invalid number of arguments")
    else:

        try:
            FileSearch(sys.argv[1])
        except ValueError:
            print("Error: Invalid datatype")
        except Exception as E:
            print("invalid inpute"+E)

 

if __name__=="__main__":
    main()