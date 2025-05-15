from MarvellousNum import CheckPrime


def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def ListPrime(listX):
    primelist=[]
    for i in range(0,len(listX),1):
        primenumberlist=CheckPrime(listX[i])
        if primenumberlist ==0:
            primelist.append(listX[i])
    return primelist
    
def SumofPrime(sumprime):
    sum=0
    for value in sumprime:
        sum=sum+value
    return sum




def main():
    print("enter length of list")
    length=int(input())
    
    dataX=Acceptnumber(length)
    prime=ListPrime(dataX)
    print("prime number list",prime)
    sumofprime=SumofPrime(prime)
    print("sum of prime number",sumofprime)


   

if __name__=="__main__":
    main()