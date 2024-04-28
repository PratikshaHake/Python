def Display(No):
   if(No!=0):
        print(No,end=" ")
        No=No-1
        Display(No)

def main():
    print("Enter a number")
    no=int(input())

    Display(no)

if __name__=="__main__":
    main() 