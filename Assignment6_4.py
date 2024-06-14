import threading

def Small(String):
    print("ID of  thread1 ",threading.get_ident())
    print("Name of thread1 is : ",threading.current_thread().name)
    count=0
    for ch in String:
        if(ch.islower()):
            count=count+1
    
    print("numberr of small character are : ",count)

def Capital(String):
    print("ID of  thread2 ",threading.get_ident())
    print("Name of thread2 is : ",threading.current_thread().name)
    count=0
    for ch in String:
        if(ch.isupper()):
            count=count+1
    
    print("numberr of capital character are : ",count)

def Digit(String):
    print("ID of  thread3 ",threading.get_ident())
    print("Name of thread3 is : ",threading.current_thread().name)
    count=0
    for ch in String:
        if(ch.isnumeric()):
            count=count+1

    print("number of digits in string are : ",count)

def main():
    print("ID of main thread ",threading.get_ident())
    print("Name of main thread is : ",threading.current_thread().name)
    print("Enter a string")
    str=input()

    small=threading.Thread(target=Small,args=(str,))
    capital=threading.Thread(target=Capital,args=(str,))
    digit=threading.Thread(target=Digit,args=(str,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

    print("Exit from main")

if __name__=="__main__":
    main()