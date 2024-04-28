Square=lambda No:No**2

def main():
    print("Enter a number")
    no=int(input())

    Sqr=Square(no)
    print("Square is : ",Sqr)


if __name__=="__main__":
    main()