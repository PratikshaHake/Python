import threading

def EvenAdd(Arr):
    sum=0
    for No in Arr:
        if(No%2==0):
            sum=sum+No

    print("Even elements Addition is : ",sum)

def OddAdd(Arr):
    sum=0
    for No in Arr:
        if(No%2!=0):
            sum=sum+No

    print("Odd elements addition : ",sum)

def main():
    print("number of elements")
    size=int(input())

    Arr=[]
    print("Enter the elements: ")
    for i in range(size):
        val=int(input())
        Arr.append(val)

    evenlist=threading.Thread(target=EvenAdd,args=(Arr,))
    oddlist=threading.Thread(target=OddAdd,args=(Arr,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("Exit from main")

if __name__=="__main__":
    main()