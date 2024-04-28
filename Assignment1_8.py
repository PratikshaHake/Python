def StarPattern(No):
    for i in range(No):
        print("*",end=" ")

def main():
    print("Enter a number")
    no=int(input())

    StarPattern(no)

if __name__=="__main__":
    main()