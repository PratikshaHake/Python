fact=1

def Factorial(No):
    global fact
    if(No!=0):
        fact=fact*No
        No=No-1
        Factorial(No)
        return fact
    
def main():
    print("Enter a number")
    no=int(input())

    Ans=Factorial(no)
    print("Factorial is : ",Ans)

if __name__=="__main__":
    main()
