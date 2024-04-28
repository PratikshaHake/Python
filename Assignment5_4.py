sum=0

def DigitSum(No):
   global sum
   if(No!=0):
        sum=sum+No%10
        No=No//10
        DigitSum(No)
        return sum


def main():
    print("Enter a number")
    no=int(input())

    Ret=DigitSum(no)
    print("Digit sum is : ",Ret)

if __name__=="__main__":
    main() 