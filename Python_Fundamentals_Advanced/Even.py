def CheckEven(No):
    if(No%2==0):
        print("Number is Even number")
    else:
        print("Number is odd")

def main():
    print("Enter a number")
    A=int(input())

    CheckEven(A)
    
main()