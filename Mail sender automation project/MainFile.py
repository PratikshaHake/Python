from CreateLog import *
from sys import *



def main():
    print("---------------Pratiksha Hake-----------")

    print("Application name :"+argv[0])
    if(len(argv)!=3):
        print("Error : Invalid number of argumets")
        exit()
    if(argv[1]=='-u') or (argv[1]=='-U'):
        print("Usage : ApplicationName AbsolutePath_of_Directory senders_emailAddress")
        exit()

    if(argv[1]=='-h') or (argv[1]=='-H'):
        print("This script is used log record of running processes")
        exit()
    
    try:
       CreateLog(argv[1])
    except ValueError:
        print("Error :Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid Input due to ",E)

if __name__=="__main__":
    main()


