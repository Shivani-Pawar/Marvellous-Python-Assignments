def sumoffact(value):
    fact=0

    for i in range(1,int(value/2)+1,1):
        
        if (value%i)==0:
            fact=fact+i

    return fact
        





def main():

    print("enter number")
    no1=int(input())
    result=sumoffact(no1)
    print("sum of Factorial is ",result)





if __name__=="__main__":
    main()