class Demo:
    Data1=11
    Data2=21

    def __init__(self,A,B):
        print("Inside constructor")
        self.No1=A
        self.No2=B
        
    def Display(self):
        print("Value of No1 from display : ",self.No1)
        print("Value of No2 from display : ",self.No2)
        print("Value of Data1 from Display :",Demo.Data1)
        print("Value of Data2 from Display :",Demo.Data2)

    @classmethod
    def Fun(cls):
        print("Value of Data1 from Fun : ",Demo.Data1)
        print("Value of Data2 from Fun : ",Demo.Data2)
        
    @staticmethod
    def Gun():
        print("Inside static method")

Demo.Fun()
Demo.Gun()
obj=Demo(5,10)
obj.Display()





    