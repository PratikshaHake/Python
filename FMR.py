from functools import reduce

def main():
    arr=[8,9,5,16,2,4,21,30,11]
    evenArr=list(filter(lambda no:(no%2==0),arr))
    ModArray=list(map(lambda no:no+2,evenArr))
    sum=reduce(lambda a,b:a+b, ModArray)
    print("Addition of even numbers using lambda",sum)


if __name__=="__main__":
    main()