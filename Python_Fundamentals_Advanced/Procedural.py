print("Demonstration of Procedural programming")
def Addition(No1,No2):
    Ans=No1+No2
    return Ans

def Substraction(No1,No2):
    Ans=No1-No2
    return Ans

def main():
    
    print("Enter a number :")
    A=int(input())

    print("Second number")
    B=int(input())

    Ans=Addition(A,B)
    print("Addition is : ",Ans)

    Ans=Substraction(A,B)
    print("Substration is : ",Ans)

if __name__=="__main__":
    main()