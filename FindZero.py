# Finding zeros in number

def FindZero(No):
    Cnt=0
    while(No>0):
        i=No%10
        if(i==0):
            Cnt+=1
        
        No=No//10

    return Cnt
    
        
def main():
    print("Enter a number")
    no=int(input())

    ZeroCnt=FindZero(no)

    print("Total count of 0's in number is: ",ZeroCnt)

if __name__=="__main__":
    main()