class BankAccount:
    
    def __init__(self,a,n,b):
        self.account_number=a
        self.name=n
        self.balance=b
        
        

    def Deposit(self):
       dep=0
       print("enter amount to be deposited")
       dep=int(input())
       self.balance=dep+self.balance
       print(dep)
        
    def Withdraw(self):
       With=0
       print("enter amount to be withdrawn")
       With=int(input())
       self.balance=self.balance-With
       print(With)

    def Display(self):
        print("balance of account is",self.balance)



def main():
    print("account numnber")
    account=int(input())
    print("name")
    name=(input())
    print("balance")
    b=int(input())

    obj=BankAccount(account,name,b)
    obj.Display()
    obj.Deposit()
    obj.Display()
    obj.Withdraw()
    obj.Display()
   



if __name__=="__main__":
    main()