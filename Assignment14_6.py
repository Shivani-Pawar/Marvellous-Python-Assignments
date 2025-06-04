class Calculator:
    
    def __init__(self,n1,n2):
        self.No1=n1
        self.No2=n2
   
        
        

    def Add(self):
        Add=0
        Add=self.No1+self.No2
        print("Addition is",Add)
       
    def Sub(self):
        Sub=0
        Sub=self.No1-self.No2
        print("Substracction is",Sub)

    
    def Mul(self):
        Mul=0
        Mul=self.No1*self.No2
        print("Multiplication  is",Mul)
       

    def Div(self):
        Div=0
        Div=self.No1/self.No2
        print("Addition is",Div)
        



def main():
    print(" numnber1")
    num1=int(input())
    print("number2")
    num2=int(input())
  

    obj=Calculator(num1,num2)
    obj.Add()
    obj.Sub()
    obj.Mul()
    obj.Div()

   



if __name__=="__main__":
    main()