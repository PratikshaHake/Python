import threading
def EvenFactor(No):
    sum=0
    for i in range(2,No,2):
        if(No%i==0):
            sum=sum+i

    print("Addition of even factors : ",sum)
    
def OddFactor(No):
    sum=0
    for i in range(1,No,2):
         if(No%i==0):
            sum=sum+i
    print("Addition of odd factors : ",sum)
    
def main():
    print("Enter a number")
    No=int(input())

    evenfactor=threading.Thread(target=EvenFactor,args=(No,))
    oddfactor=threading.Thread(target=OddFactor,args=(No,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

   

    print("Exit from main")

if __name__=="__main__":
    main()

    

        
