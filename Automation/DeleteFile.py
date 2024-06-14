import os

def main():
    print("Enter the name of file that you want to delete :")
    Fname=input()

    if os.path.exists(Fname):
        os.remove(Fname)
    else:
        print("File doesn't exists")


if __name__=="__main__":
    main()