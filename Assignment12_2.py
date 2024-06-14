import psutil
import multiprocessing
from sys import *

def DisplayProcess(name):
    print("List of running processes are :")

    print("------------------------------------")

    
  
    for proc in psutil.process_iter(['pid','name','username']):
        if proc.info['name']==name:
                print(proc.info)

    print("--------------------------------------")

def main():
    DisplayProcess(argv[1])

if __name__=="__main__":
    main()