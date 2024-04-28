def Prime(No):
    flag=False
    if (No==1):
        print("Not a prime number")
    elif(No>1):
        for i in range(2,No):
            if(No%i==0):
                flag=True
                break

        if flag:
            print("It is not a prime number")
        else:
            print("It is prime number")

def main():
    print("Enter a number")
    no=int(input())

    Prime(no)

if __name__=="__main__":
    main()