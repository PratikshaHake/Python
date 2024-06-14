#predefined function
def sub(A,B): # 0x100
    print(A-B)

def SmartSub(fptr):#0x200
    def Inner(A,B):#0x300
        if A<B :
            A,B = B,A
        return fptr(A,B) #0x100(A,B)
    return Inner 

sub=SmartSub(sub) 

def main():
    No1=int(input("Enter first number : "))
    No2=int(input("Enter second number : "))
    
    sub(No1,No2) # 0x300(No1,No2)

if __name__=="__main__":
    main()