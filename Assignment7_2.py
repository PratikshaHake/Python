class Circle:
    PI=3.14

    def __init__(self):
        self.radius=0.0
        self.Area=0.0
        self.circumference=0.0

    def Accept(self):
        print("Enter the value of radius : ")
        self.radius=float(input())

    def CalculateCircumference(self):
        self.circumference=2*Circle.PI*self.radius
    
    def CalculateArea(self):
        self.Area=Circle.PI*self.radius*self.radius

    def Display(self):
        print("Radius is : ",self.radius)
        print("Circumference is : ",self.circumference)
        print("Area of cirlce is : ",self.Area)

def main():
    obj1=Circle()
    obj1.Accept()
    obj1.CalculateCircumference()
    obj1.CalculateArea()
    obj1.Display()

if __name__=="__main__":
    main()