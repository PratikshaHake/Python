from functools import reduce

def chkPrime(No):
    flag=True
    if(No>1):
        for i in range(2,No):
            if(No%i==0):
                flag=False
                break
        return flag

def chkMax(A,B):
    max=0
    if(A>B):
        max=A
    else:
        max=B

    return max
        

def main():
    Data=list()
    print("Enter number of elements")
    size=int(input())

    for no in range(size):
        val=int(input())
        Data.append(val)

    print("Data list is : ",Data)
    
    FData=list(filter(chkPrime,Data))
    print("list after Filter activity :",FData)

    MData=list(map((lambda No:No*2),FData))
    print("list after map activity : ",MData)

    max=reduce(chkMax, MData)
    print("Maximum number is : ",max)

if __name__=="__main__":
    main()