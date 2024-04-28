def Pattern(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()    

def main():
    print("Enter a number: ")
    no=int(input())

    Pattern(no)

if __name__=="__main__":
    main()