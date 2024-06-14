import os

def main():
    print("Enter the name of file taht you want to search..")
    Fname=input()

    if os.path.exists(Fname):
        print("File is present in the current directory")
    else:
        print("File dosen't present in current directory")

if __name__=="__main__":
    main()
    