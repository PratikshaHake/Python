import MarvellousNum
def ListPrime(no):
    Arr=list()
    for i in range(no):
        val=int(input())

        if(MarvellousNum.ChkPrime(val)==True):
            Arr.append(val)

    return Arr

def AddList(Arr):
    sum=0
    for i in range(len(Arr)):
        sum=sum+Arr[i]

    return sum


def main():
    Arr=list()
    print("Enter Number of elements : ")
    no=int(input())

    Arr=ListPrime(no)
    print(Arr)
    
    Ans=AddList(Arr)
    print("Addition of prime numbers is : ",Ans)


   


if __name__=="__main__":
    main()
