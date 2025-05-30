
class Number:
        
        
        def __init__(self,N):
            self.No1=N
            
            

        def ChkPrime(self):
             for i in range(2,self.No1):
                  if(self.No1%i==0):
                       return False
             return True                
            
            


        
        def ChkPerfect(self):
             sum=0
             for i in range(1,self.No1):
                  if(self.No1%i==0):
                       sum=sum+i
             if(sum==self.No1):
                  return True
             else:
                  return False
            

        def Factors(self):
             for i in range(1,self.No1):
                  if(self.No1%i==0):
                       print(i)
                 
        
        def SumFactors(self):
             sum=0
             for i in range(1,self.No1):
                  if(self.No1%i==0):
                       sum=sum+i
             return sum
             

        

def main():
    ret=False
    print("enter number")
    num=int(input())
    obj1=Number(num)
    ret=obj1.ChkPrime()
    print("prime",ret)
    ret=obj1.ChkPerfect()
    print("perfect",ret)
    obj1.Factors()
    ret=obj1.SumFactors()
    print("sum of factors",ret)


    ret1=False
    print("enter number")
    num1=int(input())
    obj2=Number(num1)
    ret1=obj2.ChkPrime()
    print("prime",ret1)
    ret1=obj2.ChkPerfect()
    print("perfect",ret1)
    obj2.Factors()
    ret1=obj2.SumFactors()
    print("sum of factors",ret1)
    
    


   


if __name__=="__main__":
    main()
