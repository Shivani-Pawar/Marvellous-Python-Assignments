
class Product:
    def __init__(self,n,p):
        self.name=n
        self.price=p
    
    def __eq__(self,second):
        if second.price==self.price:
            return True
        return False 
   
        




def main():
    obj1=Product("Shivani",200)
    obj2=Product("Sangram",500)
    print(obj1==obj2)
  

    
    

   



if __name__=="__main__":
    main()