class BankAccount:
    ROI=10.5
    def __init__(self):
        self.Name=input("Enter Name :")
        self.Amount=int(input("Enter Amount :"))

    def Deposit(self):
        Amt=int(input("Enter value that you want to deposit :"))
        self.Amount+=Amt
        print("Total balance after Deposit is :",self.Amount)

    def Withdraw(self):
        Amt=int(input("Enter amount that you want to withdraw : "))
        if(Amt>self.Amount):
            print("Insufficient balance")
        else:
            self.Amount-=Amt
        print("Total balance After withdrawal is :",self.Amount)
        
    def CalculateInterest(self):
        interest=self.Amount*BankAccount.ROI/100
        print("Simple interest is : ",interest)
    
    def Display(self):
        print("Name is : ",self.Name)
        print("Toatl balance in your account : ",self.Amount)
    
def main():
    obj1=BankAccount()
    
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

    obj2=BankAccount()
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()

if __name__=="__main__":
    main()
    
        