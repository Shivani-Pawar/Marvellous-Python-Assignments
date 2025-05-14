     
            

        
       

    
        





def main():

    print("enter number")
    no1=int(input())        #123
    count=0
       #3
    while (no1>0):
        digit=no1%10
        
        count=count+digit 

        no1//=10
      

    print("count is",count)




   

  





if __name__=="__main__":
    main()