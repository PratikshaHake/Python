def CreateList(n):
    Arr=list()
    for i in range(n):
        val=int(input())
        Arr.append(val)

    return Arr

def FindFreq(Arr,Val):
    Cnt=0
    for i in range(len(Arr)):
        if(Val==Arr[i]):
            Cnt=Cnt+1

    return Cnt
            

def main():
    print("Enter number of elements: ")
    no=int(input())

    Arr=CreateList(no)

    print("Enter element for search")
    Val=int(input())

    Ans=FindFreq(Arr,Val)
    print("Frequency of element is : ",Ans)


if __name__=="__main__":
    main()
