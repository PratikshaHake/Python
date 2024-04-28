def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    print("Enter a Number")
    No1=int(input())
    print("Enter second Number")
    No2=int(input())

    Result=Add(No1,No2)
    print("Addition is :",Result)


if __name__=="__main__":
    main()

