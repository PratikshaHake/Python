def StarPattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end=" ")

        print()

def main():
    print("Enter a number")
    no=int(input())

    StarPattern(no)

if __name__=="__main__":
    main()