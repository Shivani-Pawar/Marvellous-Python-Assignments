
class BankAccount:
        ROI=10.5
        
        def __init__(self,N,A):
            self.Name=N
            self.Amount=A
            

        def Deposit(self):
            
            return self.Amount+BankAccount.ROI


        
        def Withdraw(self):
            
            return self.Amount-BankAccount.ROI
        
        def CalculateIntrest(self):
             return self.Amount*  BankAccount.ROI

        def Display(self):
             print("The name is",self.Name)
             print("The amount is ",self.Amount)

def main():
    
    print("enter name")
    name=input()
    print("enter amount")
    a=int(input())
    obj1=BankAccount(name,a)
    obj1.Display() 
    ret=obj1.Deposit()
    print("the deposit ",ret)
    ret2=obj1.Withdraw()
    print("the withdrawn",ret2)
    ret3=obj1.CalculateIntrest()
    print("the intrest",ret3)


    print("enter name")
    name2=input()
    print("enter amount")
    a2=int(input())

    obj2=BankAccount(name2,a2)
    obj2.Display() 
    ret4=obj2.Deposit()
    print("the deposit ",ret4)
    ret5=obj2.Withdraw()
    print("the withdraw ",ret5)
    ret6=obj2.CalculateIntrest()
    print("inteest is",ret6)
    
    



if __name__=="__main__":
    main()
