def ChkNum(No):
    if(No%2==0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Please enter a number")
    No=int(input())
    ChkNum(No)

if __name__=="__main__":
    main()