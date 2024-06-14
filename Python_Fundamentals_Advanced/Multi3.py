def Even(No):
    x=2
    for i in range(No):
       print(x)
       x=x+2

def Odd(No):
   x=1
   for i in range(No):
       print(x)
       x=x+1

def main():
    print("Enter a number")
    no=int(input())
    print("List of Even numbers:")
    Even(no)
    print("List of Odd numbers:")
    Odd(no)
   
if __name__=="__main__":
    main()