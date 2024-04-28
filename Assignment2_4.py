def FactorAdd(No):
    Sum=0
    for i in range(1,No):
        if(No%i==0):
            Sum=Sum+i
    return Sum

def main():
    print("Enter a number")
    no=int(input())

    Result=FactorAdd(no)
    print("Addition of factors is:",Result)

if __name__=="__main__":
    main()