class Arithematic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
        self.Ans=0
    
    def Accept(self):
        print("Enetr first value : ")
        self.Value1=int(input())

        print("Enetr second value : ")
        self.Value2=int(input())

    def Addition(self):
        self.Ans=self.Value1+self.Value2
        print("Addition is : ",self.Ans)

    def Substraction(self):
        self.Ans=self.Value1-self.Value2
        print("Substraction is : ",self.Ans)

    def Multiplication(self):
        self.Ans=self.Value1*self.Value2
        print("Multiplication is : ",self.Ans)

    def Division(self):
        if (self.Value2!=0):
            self.Ans=self.Value1/self.Value2
        else:
            print("Please enter valid second number other than 0 ")
        
        print("Division is : ",self.Ans)

def main():
    obj1=Arithematic()
    obj2=Arithematic()
    obj3=Arithematic()
    obj4=Arithematic()
    obj5=Arithematic()
    
    print("Operations from object1 :")
    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()
   
    print("Operations from object2 :")
    obj2.Accept()
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()

    print("Operations from object3 :")
    obj3.Accept()
    obj3.Addition()
    obj3.Substraction()
    obj3.Multiplication()
    obj3.Division()

    print("Operations from object4 :")
    obj4.Accept()
    obj4.Addition()
    obj4.Substraction()
    obj4.Multiplication()
    obj4.Division()

    print("Operations from object5 :")
    obj5.Accept()
    obj5.Addition()
    obj5.Substraction()
    obj5.Multiplication()
    obj5.Division()

if __name__=="__main__":
    main()