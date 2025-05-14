
import math            
            

        
       

    
        





def main():

    print("enter number")
    no1=int(input())        #123
    count=0
       #3
    while (no1>0):
        digit=no1%10
        if (digit >0):
            count=count+1 

        no1//=10
      

    print("count is",count)




   

  





if __name__=="__main__":
    main()