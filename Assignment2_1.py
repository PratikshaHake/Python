import Arithmetic 

def main():
    print("Enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    Result=Arithmetic.Add(No1,No2)
    print("Addition is: ",Result)

    Result=Arithmetic.Sub(No1,No2)
    print("Substraction is: ",Result)

    Result=Arithmetic.Mul(No1,No2)
    print("Multiplication is: ",Result)
     
    if(No2==0):
        print("You can not divide a number by zero")
        print("Please enter a valid number other than zero")
        return

    Result=Arithmetic.Div(No1,No2)
    print("Division is: ",Result)


if __name__=="__main__":
    main()
