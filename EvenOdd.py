#Check whether the number is even or odd

def EvenOdd(No):
    if(No%2==0):
        print("Even")
    else:
        print("Odd")

def main():
    print("Enter a number")
    no=int(input())

    EvenOdd(no)

if __name__=="__main__":
    main()