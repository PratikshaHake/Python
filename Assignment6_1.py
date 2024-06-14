import threading
def Even():
    print("List of even numbers")
    x=2
    for i in range(10):
        
        print(x)
        x=x+2

def Odd():
    print("List of odd numbers")
    x=1
    for i in range(10):
        print(x)
        x=x+2

def main():
    even=threading.Thread(target=Even,args=())
    odd=threading.Thread(target=Odd,args=())

    even.start()
    odd.start()

    even.join()
    odd.join()

if __name__=="__main__":
    main()

