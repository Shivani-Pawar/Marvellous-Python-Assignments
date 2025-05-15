
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def Maximum(listX):
    for i in listX:
        for j in listX:
            if i>j:
                j=i
    return j




def main():
    print("enter length of list")
    length=int(input())
    dataX=Acceptnumber(length)
    maxX=Maximum(dataX)
    print("maximum of numbers in list is",maxX)
    

if __name__=="__main__":
    main()