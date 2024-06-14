from functools import reduce
ChkEven=lambda No:No%2==0
Increase=lambda No:No+1
Add=lambda A,B:A+B
def main():
    Data=list()
    print("Enter number of element")
    size=int(input())

    print("Enter the elements : ")
    for i in range(size):
        val=int(input())
        Data.append(val)

    print("Data from input list :",Data)

    FData=list(filter(ChkEven, Data))
    print("Data after filter activity : ",FData)

    MData=list(map(Increase,FData))
    print("Data after map activity : ",MData)

    RData=reduce(Add, MData)
    print("Data after reduce activity : ",RData)

if __name__=="__main__":
    main()