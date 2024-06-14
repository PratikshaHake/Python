import sys

def main():
    print("Compare contents of ",sys.argv[1]," and ",sys.argv[2])
    fobj1=open(sys.argv[1],"r")
    str1=fobj1.readlines()

    fobj2=open(sys.argv[2],"r")
    str2=fobj2.readlines()

    if(str1==str2):
        print("Success")
    else:
        print("Failure")

if __name__=="__main__":
    main()