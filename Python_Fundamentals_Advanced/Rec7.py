

def DisplayR(No):
   
    if(No!=0):
        print(No)
        No=No-1
        DisplayR(No)
       

def main():
    print("Enter a number")
    no=int(input())
    DisplayR(no)

if __name__=="__main__":
    main()