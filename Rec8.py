i=1
fact=1
def Fact(No):
    global i
    global fact

    if(No>=1):
        fact=fact*No
        No=No-1
        Fact(No)

    return fact


def main():
    print("Enter the number")
    no=int(input())

    factorial=Fact(no)
    print("Factorial is:",factorial)

if __name__=="__main__":
    main()