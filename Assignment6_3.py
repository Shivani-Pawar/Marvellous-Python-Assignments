
def Multiply(value):
    
    i=1
    sum=0
    while(i<=10):

        print(value,"*",i,"=",value*i)
        i=i+1
       
            
            
        
    

def main():
    print("enter number")
    no=int(input())
    Multiply(no)
    


if __name__=="__main__":
    main()