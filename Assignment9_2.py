import os

def main():
    print("Enter the name of file that you want to open")
    Fname=input()

    if os.path.exists(Fname):
        fobj=open(Fname,"r")

        for line in fobj: 
            print(line)


if __name__=="__main__":
    main()