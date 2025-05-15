
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def Frequency(listX,no):
    count=0
    for i in range(0,len(listX),1):
        if no == listX[i]:
            count=count+1
    return count 





def main():
    print("enter length of list")
    length=int(input())
    print("enter number you want to serach in  list")
    freq=int(input())
    dataX=Acceptnumber(length)
    f=Frequency(dataX,freq)
    print("the number in list is ",f,"time")
    

if __name__=="__main__":
    main()