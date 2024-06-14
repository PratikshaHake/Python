import os
import sys

def main():
    print("Enter a file name that you want to write contents : ")
    Fname=input()

    fobj=open(sys.argv[1],"r")

    str=fobj.read()

    fobj1=open(Fname,"a")
    fobj1.write(str)

if __name__=="__main__":
    main()