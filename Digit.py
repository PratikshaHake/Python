#PRint the count of digits in the number

def Digit(No):
    Cnt=0
    while(No>0):
        Cnt+=1
        No=No//10

    return Cnt
        
def main():
    print("Enter a number")
    no=int(input())

    Count=Digit(no)
    print("Total number of digits:",Count)

if __name__=="__main__":
    main()
