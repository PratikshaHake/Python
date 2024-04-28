def Length(Data):
    Cnt=len(Data)
    return Cnt

def main():
    print("Enter name")
    name=input()

    Cnt=Length(name)
    print(Cnt)

if __name__=="__main__":
    main()