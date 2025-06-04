class Vehicle:
    
    def company(self):
        print("This vehicle is lamborg")
   
        
        

class Car(Vehicle):
    
    def company(self):
       
       print("inside derived menthod")
        



def main():
    obj=Car()
    obj.company()
  

    
    

   



if __name__=="__main__":
    main()