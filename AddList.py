def Addition(Data):
    Sum=0

    for no in Data:
        Sum+=no

    return Sum

def main():
    print("Enter the number of element that you want in the list")
    size=int(input())

    Arr=list()

    print("Enter elements")
    for No in range(size):
        No=int(input())
        Arr.append(No)
    print("Entered elements are: ",Arr)
    Result=Addition(Arr)
    print("Addition of lis is: ",Result)

        
if __name__=="__main__":
    main()