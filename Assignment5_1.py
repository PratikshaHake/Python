i=0
def Display(No):
    global i
    if(i<No):
        print("*",end=" ")
        i=i+1
        Display(No)

def main():
    print("Enter a number")
    no=int(input())

    Display(no)

if __name__=="__main__":
    main() 