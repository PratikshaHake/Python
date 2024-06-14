import os

def Cube(No):
    print("PID is :",os.getpid())
    return No**3

def main():
    Arr=[10,20,30,40]
    result=[]

    for i in Arr:
        result.append(Cube(i))

    print(result)
   
if __name__=="__main__":
    main()