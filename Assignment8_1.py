class BookStore:
    NoOfBooks=0
    def __init__(self):
        self.Name=input("Enter book name : ")
        self.Author=input("Enter author name : ")
        BookStore.NoOfBooks+=1

    def Display(self):
        print(self.Name+" By ",self.Author,". No of books : ",BookStore.NoOfBooks)

def main():
    obj1=BookStore()
    obj1.Display()

    obj2=BookStore()
    obj2.Display()

if __name__=="__main__":
    main()