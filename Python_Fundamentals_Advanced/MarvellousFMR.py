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