import multiprocessing

def Even(No):
    print("List of Even numbers:")
    x=2
    for i in range(No):
       print(x)
       x=x+2

def Odd(No):
    print("List of Odd numbers:")
    x=1
    for i in range(No):
       print(x)
       x=x+1

def main():
    print("Enter a number")
    no=int(input())

    p1=multiprocessing.Process(target=Even,args=(no,))
    p2=multiprocessing.Process(target=Odd,args=(no,))
    
    
    p1.start()
  
    p2.start()

    p1.join()
    p2.join()
  
    print("End of process")
   
if __name__=="__main__":
    main()