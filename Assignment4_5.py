from functools import reduce
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def rangefunc(no):
        count=0
        for i in range(2,no,1):
            if no%i!=0:
                count=count+1
        
        if count==0:
            return no

def Square(no1):
    return no1*2

def Product(value1,value2):
    if value1>value2:
        return value1
    else:
        return value2




def main():
    print("enter length of list")
    length=int(input())
    dataX=Acceptnumber(length)
    resultoffilter=list(filter(rangefunc,dataX))
    print("output after filter",resultoffilter)

    resultofmap=list(map(Square,resultoffilter))
    print("output after map",resultofmap)

    resultofreduce=reduce(Product,resultofmap)
    print("output of reduce",resultofreduce)


    
    

if __name__=="__main__":
    main()