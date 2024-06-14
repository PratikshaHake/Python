i=1

def DisplayR(No):
    global i
   
    if(i<=No):
        print(i)
        i=i+1
        DisplayR(No)
       

def main():
    print("Enter a number")
    no=int(input())
    DisplayR(no)

if __name__=="__main__":
    main()