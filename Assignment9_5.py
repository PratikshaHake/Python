import sys

def main():
    count=0
    print("Enter name of file :")
    Fname=input()
    print("Enter a string that you want to search :")
    Str=input()

    fobj=open(Fname,"r")
    lines=fobj.readlines()

    for row in lines:
        if(row.find(Str)!=-1):
            count=count+1
    print("Frequency of ",Str ," is :",count)

if __name__=="__main__":
    main()