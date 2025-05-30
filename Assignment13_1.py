
class BookStore:
        NoOfBooks=0
        
        def __init__(self,N,A):
            self.Name=N
            self.Author=A
            BookStore.NoOfBooks=BookStore.NoOfBooks+1

        def Display(self):
             print(self.Name,"by",self.Author,".","No of books:",BookStore.NoOfBooks)




def main():
    print("enter book name")
    name= input()
    print("enter author of book")
    Author=input()

    print("enter book name")
    nam2= input()
    print("enter author of book")
    auth2=input()

    obj1=BookStore(name,Author)
    obj1.Display() 
    obj2=BookStore(nam2,auth2)
    obj2.Display() 




if __name__=="__main__":
    main()
