
def main():
    print("Enter the number of elements you want in list:")
    No=int(input())
    Arr=list()
    print("Enter the elemts: ")

    for i in range(No):
        val=int(input())
        Arr.append(val)
    print(Arr)

if __name__=="__main__":
    main()