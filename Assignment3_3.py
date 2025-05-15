
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def Minimum(listX):
    for i in range(1,len(listX),1):
        if listX[i] < listX[i+1]:
            k=i
        else:
            k=i+1
               





def main():
    print("enter length of list")
    length=int(input())
    dataX=Acceptnumber(length)
    minX=Minimum(dataX)
    print("minimum of numbers in list is",minX)
    

if __name__=="__main__":
    main()