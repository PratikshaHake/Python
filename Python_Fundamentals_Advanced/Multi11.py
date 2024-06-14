import multiprocessing
import os
import time

def Fun(No):
    sum=0
    print("PID is :",os.getpid())
    for i in range(No):
        sum=sum+(No**3)
    return sum

def main():
    starttime=time.time()
    Arr=[100000,200000,300000,400000,500000,600000,7000000,800000,900000,1000000,1100000,1200000,1300000]

    result=[]

    p=multiprocessing.Pool()
    result=p.map(Fun,Arr)
    p.close()
    p.join()

    print(result)
    endtime=time.time()
    print("Time required for execution :",endtime-starttime)
   
if __name__=="__main__":
    main()