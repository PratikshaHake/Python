Multi=lambda A,B: A*B

def main():
    print("Enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    Ans=Multi(No1,No2)
    print("Multiplication is : ",Ans)

if __name__=="__main__":
    main()