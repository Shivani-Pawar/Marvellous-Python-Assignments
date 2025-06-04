class Book:
    def __init__(self):
        self.__price=0
        
        

    def Accept(self):
        print("enter price of book")
        self.__price=int(input())

    def Set(self):
        print("the price of book is",self.__price)


def main():
    



    obj=Book()
    obj.Accept()
    obj.Set()
    


if __name__=="__main__":
    main()