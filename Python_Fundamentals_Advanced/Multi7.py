import threading
import os

def Even(No):
    print("Pid of even process : ",os.getpid())

    print("List of Even numbers:")
    x=2
    for i in range(No):
       print("Even : ",x)
       x=x+2

def Odd(No):
    print("Pid of odd process : ",os.getpid())
    print("List of Odd numbers:")
    x=1
    for i in range(No):
       print("Odd : ",x)
       x=x+1

def main():
    print("Pid of main process :",os.getpid())
    print("Enter a number")
    no=int(input())

    p1=threading.Thread(target=Even,args=(no,))
    p2=threading.Thread(target=Odd,args=(no,))
    
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print("End of process")
   
if __name__=="__main__":
    main()