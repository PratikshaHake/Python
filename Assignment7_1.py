class Demo:
    Value=10

    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Fun(self):
        print("Value of no1 from Fun : ",self.no1)
        print("Value of no2 from Fun : ",self.no2)

    def Gun(self):
        print("Value of no1 from Gun : ",self.no1)
        print("Value of no2 from Gun : ",self.no2)

def main():
    print("Enter values for object1")
    A=int(input())
    B=int(input())

    obj1=Demo(A,B)

    print("Enter values for object1")
    A=int(input())
    B=int(input())

    obj2=Demo(A,B)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__=="__main__":
    main()
