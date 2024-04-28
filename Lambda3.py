ChkEven=lambda A: A%2==0
def EvenOdd(No):
   
   return (No%2==0)

def main():
    print("Enter a number")
    no=int(input())
    Ret=ChkEven(no)

    if Ret==True:
        print("Even")
    else:
        print("Odd")

if __name__=="__main__":
    main()