import threading
import os

def PrintNum():
    print("1 to 50 numbers :")
    for No in range(1,51):
        print(No)

def PrintRevNum():
    print("50 to 1 numbers")
    for No in range(51,0,-1):
        print(No)

def main():
    thread1=threading.Thread(target=PrintNum,args=())
    thread2=threading.Thread(target=PrintRevNum,args=())

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    print("Exit from main")

if __name__=="__main__":
    main()