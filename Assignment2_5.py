def CheckPrime(value):
    count=0

    for i in range(2,value,1):
        
        if (value%i) == 0:
            count=count +1
    return count   

    
        





def main():

    print("enter number")
    no1=int(input())
    res=CheckPrime(no1)
    #print(res)
    if res==0:
        print("prime number")
    elif res>0:
        print("not prime number")  

  





if __name__=="__main__":
    main()