import sys

def Addition(*No):
    Ans=0
    i=1
    for i in No:
        Ans+=i
    return Ans
    
def main():
    print("Welcome to the application: "+sys.argv[0])

    if(len(sys.argv)<3):
        print("Invalid number of arguments")
        print("Please provide at least 2 numeric arguments to perform addition")
        return
    
    Result=Addition(eval(sys.argv))
    print("Addition is: ",Result)


if __name__=="__main__":
    main()