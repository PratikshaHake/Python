cube=lambda A:A**3

def main():
    print("Enter a number")
    no=int(input())

    Ret=cube(no)
    print("Cube is : ",Ret)

if __name__=="__main__":
    main()