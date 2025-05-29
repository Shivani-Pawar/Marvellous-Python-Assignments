factX=1
def factorial(value):
    global factX
    if(value>=1):
      
        factX=factX*value
        value=value-1
        factorial(value)
    return factX




def main():
    print("enter number")
    no=int(input())
    fact=factorial(no)
    print(fact)




if __name__=="__main__":
    main()
