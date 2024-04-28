def CreateList(n):
    Arr=list()
    for i in range(n):
        val=int(input())
        Arr.append(val)

    return Arr

def AddList(Arr):
    sum=0
    for i in range(len(Arr)):
        sum=sum+Arr[i]

    return sum

def main():
    print("Enter number of elements: ")
    no=int(input())

    Arr=CreateList(no)
    Ans=AddList(Arr)

    print("Addition of list is : ",Ans)


if __name__=="__main__":
    main()
