class Arithmetic:
    def __init__(self):
        self.Value=int(input("Enter a number : "))

    def ChkPrime(self):
    
        if(self.Value>2):
            for i in range(2,self.Value):
                if(self.Value%i==0):
                    return False
                    break
                else:
                    return True
    
    
    def ChkPerfect(self):
        sum=0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                sum+=i
        
        if(self.Value==sum):
            return True
        else:
            return False
        
        

    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                sum+=i
            
        return sum
    
    def Factors(self):
        Factors=[]
        for i in range(1,self.Value):
            if(self.Value%i==0):
                Factors.append(i)

        return Factors

def main():
    obj1=Arithmetic()
    Ret=obj1.ChkPrime()
  
    if(Ret==True):
        print("Number is prime")
    else:
        print("Number is not prime")

    Ret=obj1.ChkPerfect()
   
    if(Ret==True):
        print("Number is perfect")
    else:
        print("Number is not perfect")

    factor=obj1.Factors()
    print("Factors are : ",factor)

    sum=obj1.SumFactors()
    print("Sum of factors is : ",sum)

if __name__=="__main__":
    main()
