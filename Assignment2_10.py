def DigitSum(No):
    Sum=0
    digit=0
    while(No!=0):
        digit=No%10
        Sum=Sum+digit
        No=No//10

    return Sum


def main():
    print("Enter a number")
    no=int(input())

    Result=DigitSum(no)
    print("Addition is: ",Result)

if __name__=="__main__":
    main()

