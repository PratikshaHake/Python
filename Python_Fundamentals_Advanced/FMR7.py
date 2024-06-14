from MarvellousFMR import *

def main():
    Data=list()
    print("Enter number of element")
    size=int(input())

    print("Enter the elements : ")
    for i in range(size):
        val=int(input())
        Data.append(val)

    print("Data from input list :",Data)

    FData=list(filterX(ChkEven, Data))
    print("Data after filter activity : ",FData)

    MData=list(mapX(Increase,FData))
    print("Data after map activity : ",MData)

    RData=reduceX(Add, MData)
    print("Data after reduce activity : ",RData)

if __name__=="__main__":
    main()