
def Fact(value):
    
    
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    return fact
            
            
        
    

def main():
    print("enter number")
    no=int(input())
    f=Fact(no)
    print(f)
    


if __name__=="__main__":
    main()