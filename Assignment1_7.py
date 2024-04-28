def DivideByFive(No):
    if(No%5==0):
        return True
    else:
        return False
    
def main():
    print("Enter a number")
    no=int(input())

    Result=DivideByFive(no)

    print(Result)

if __name__=="__main__":
    main()