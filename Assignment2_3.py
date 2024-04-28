def Factorial(No):
    fact=1

    for i in range(1,No+1):
       fact=fact*i

    return fact

def main():
    print("Enter a number")
    no=int(input())
     
    if(no<0):
        print("Can not calculate factorial of negative number")
        return
    
    if(no==0):
        print("Factorial is 1")
        return

    Result=Factorial(no)

    print("Factorial is: ",Result)
    

if __name__=="__main__":
    main()