def Fact(value):
    fact=1
    for i in range(1,value+1,1):
        fact=fact*i

    return fact
        





def main():

    print("enter number")
    no1=int(input())
    result=Fact(no1)
    print("Factorial is ",result)





if __name__=="__main__":
    main()