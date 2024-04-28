from functools import reduce
def main():
    Data=list()
    print("Enter number of elements")
    size=int(input())

    for no in range(size):
        val=int(input())
        Data.append(val)

    print("Data list is : ",Data)
    
    FData=list(filter(lambda No:(No>=70 or No==90),Data))
    print("list after Filter activity :",FData)

    MData=list(map((lambda No:No+10),FData))
    print("list after map activity : ",MData)

    Product=reduce(lambda A,B:A*B, MData)
    print("Product is : ",Product)

if __name__=="__main__":
    main()