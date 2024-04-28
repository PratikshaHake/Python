import os
import multiprocessing

def Task1(No):
    print("Executing first task")
    print("PID of task1 : ",os.getpid())
    print("Parent ID : ",os.getppid())

def Task2(No):
    print("Executing second task")
    print("PID of task2 : ",os.getpid())
    print("Parent ID : ",os.getppid())

def main():
    print("PID of running process : ",os.getpid())
    print("PID of parent process ie command prompt is: ",os.getppid())

    value=11

    p1=multiprocessing.Process(target=Task1,args=(value,))
    p2=multiprocessing.Process(target=Task2,args=(value,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

if __name__=="__main__":
    main()