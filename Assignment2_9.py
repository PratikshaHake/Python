def Digit(No):
    Cnt=0

    if No==0:
        Cnt=1
    
    while(No!=0):
        No=No//10
        Cnt=Cnt+1

    return Cnt


def main():
    print("Enter a number")
    no=int(input())

    Result=Digit(no)
    print("Digits of given number are: ",Result)

if __name__=="__main__":
    main()

