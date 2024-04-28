def CreateList(n):
    Arr=list()
    for i in range(n):
        val=int(input())
        Arr.append(val)

    return Arr

def FindMin(Arr):

    min=Arr[0]
    for i in range(1,len(Arr)-1):
        if(min>Arr[i]):
            min=Arr[i]
    
    return min
            

def main():
    print("Enter number of elements: ")
    no=int(input())

    Arr=CreateList(no)
    Ans=FindMin(Arr)

    print("Minimum number from list is : ",Ans)


if __name__=="__main__":
    main()
