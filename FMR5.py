
ChkEven=lambda No:No%2==0
Increase=lambda No:No+1
Add=lambda A,B:A+B

def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)

    return Result


def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        val=Task(no)
        Result.append(val)

    return Result
        

def reduceX(Task,Elements):
    Ans=0
    for no in Elements:
        Ans=Task(Ans,no)

    return Ans

def main():
    Data=[11,14,20,23,18,16,15,20]
    print("Data from input list :",Data)

    FData=list(filterX(ChkEven, Data))
    print("Data after filter activity : ",FData)

    MData=list(mapX(Increase,FData))
    print("Data after map activity : ",MData)

    RData=reduceX(Add, MData)
    print("Data after reduce activity : ",RData)

if __name__=="__main__":
    main()