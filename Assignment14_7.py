class Person:
    
    def __init__(self,n,a):
        self.Name=n
        self.Age=a
   
        
        

class Teacher(Person):
    def __init__(self,name,Age,sub,sal):
        self.Subject=sub
        self.Salary=sal
        super().__init__(name,Age)

    def Display(self):
        print("name ",self.Name)
        print("Age",self.Age)
        print("sub",self.Subject)
        print("salary is",self.Salary)
        



def main():
    print("name of person")
    name=(input())
    print("Age of person")
    age=int(input())
    print("subject")
    subject=input()
    print("salary")
    salary=int(input())
  

    obj=Teacher(name,age,subject,salary)
    obj.Display()
    

   



if __name__=="__main__":
    main()