from functools import reduce
def Acceptnumber(value):
    data=[]
    print("enter numbers")
    for i in range(1,value+1,1):
        no1=int(input())
        data.append(no1)
    return data    

def rangefunc(no):
    if (no >70 and no<90):
        return no

def add(added):
    return added+10

def Product(value1,value2):
    return value1*value2




def main():
    print("enter length of list")
    length=int(input())
    dataX=Acceptnumber(length)
    resultoffilter=list(filter(rangefunc,dataX))
    print("output after filter",resultoffilter)

    resultofmap=list(map(add,resultoffilter))
    print("output after map",resultofmap)

    resultofreduce=reduce(Product,resultofmap)
    print("output of reduce",resultofreduce)


    
    

if __name__=="__main__":
    main()