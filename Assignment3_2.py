def CreateList(n):
    Arr=list()
    for i in range(n):
        val=int(input())
        Arr.append(val)

    return Arr

def FindMax(Arr):

    max=Arr[0]
    
    for i in range(1,len(Arr)-1):

        if(max<Arr[i]):
            max=Arr[i]
    
    return max
            

def main():
    print("Enter number of elements: ")
    no=int(input())

    Arr=CreateList(no)
    Ans=FindMax(Arr)

    print("Maximum number from list is : ",Ans)


if __name__=="__main__":
    main()
