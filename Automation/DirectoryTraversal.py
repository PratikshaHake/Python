import os

def main():
    print("Enter the name of directory that you want to scan : ")
    Dname=input()

    print("List of files in folder are :")

    for foldername,subfoldername, files in os.walk(Dname):
        for fname in files:
            print(fname)
    
if __name__=="__main__":
    main()