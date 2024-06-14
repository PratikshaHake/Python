def DisplayFor():
    print("Inside Display of for loop")
    for i in range(1,6):
        print(i)

def DisplayWhile():
    print("Inside Display of while loop")
    i=1
    while(i<6):
        print(i)
        i=i+1

def main():
    
    DisplayFor()
    DisplayWhile()

if __name__=="__main__":
    main()