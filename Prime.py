# Check whether the number is prime or not
def Prime(No):
    flag=False
    if No==1:
        print("Not prime")
    
    if No>1:
        for i in range(2,No):
            if(No%i==0):
                flag=True
                break

        if flag:
            print("Not  Prime number")
        else:
            print("Prime number")

def main():
    print("Enter a number :")
    no=int(input())

    Prime(no)

if __name__=="__main__":
    main()
