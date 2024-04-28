def Pattern(No):
    for i in range(No):
        for j in range(i,No):
            print("*",end=" ")

        print()

def main():
    print("Enter a number")
    no=int(input())

    Pattern(no)

if __name__=="__main__":
    main()