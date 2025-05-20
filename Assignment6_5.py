
def Prime(value):
    
    
    count=0
    for i in range(2,value):
        if(value%i==0):
            count=count+1
    if(count==0):
        print("prime number")
    else:
        print("not prime")
            
            
        
    

def main():
    print("enter number")
    no=int(input())
    Prime(no)
    
    


if __name__=="__main__":
    main()