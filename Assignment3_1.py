
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def Sumofdata(listX):
    sum=0
    for i in listX:
        sum=sum+i
    return sum



def main():
    print("enter length of list")
    length=int(input())
    dataX=Acceptnumber(length)
    add=Sumofdata(dataX)
    print("addition of numbers in list is",add)
    

if __name__=="__main__":
    main()