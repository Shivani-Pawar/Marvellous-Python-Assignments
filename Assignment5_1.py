def sum(no1,no2):
    Ans=0
    Ans=no1+no2
    return Ans




def Sub(no1,no2):
    Ans=0
    Ans=no1-no2
    return Ans


def Multi(no1,no2):
    Ans=0
    Ans=no1*no2
    return Ans



def Div(no1,no2):
    Ans=0
    Ans=no1/no2
    return Ans

def main():

    print("Enter number 1")
    value1=int(input())
    print("Enter number 2")
    value2=int(input())

    ret1=sum(value1,value2)
    print("The additon is",ret1)
    ret2=Sub(value1,value2)
    print("The Substraction is",ret2)
    ret3=Multi(value1,value2)
    print("The Multiplication  is",ret3)
    ret4=Div(value1,value2)
    print("The Division is",ret4)





    

if __name__=="__main__":
    main()