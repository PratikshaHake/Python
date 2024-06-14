print("Demonstration of Functional")

Addition=lambda No1,No2:No1+No2
Substraction=lambda No1,No2:No1-No2


print("Enter a number :")
A=int(input())

print("Second number")
B=int(input())

Ans=Addition(A,B)
print("Addition is : ",Ans)

Ans=Substraction(A,B)
print("Substration is : ",Ans)

