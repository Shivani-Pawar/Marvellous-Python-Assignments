from functools import reduce


def Prime(no):
    count=0
    if no >1:
        for i in range(2,no):
            if(no%i==0):
                print(i)
                count=count+1
        print(count)
        if count==0:
            return no


conditionmap=lambda no:no**2

conditionreduce =lambda A,B:A+B


def main():
    print("enter size")
    size=int(input())
    
    print("enter number in list")
    inputlist=[]
    for i in range(size):
        no=int(input())
        inputlist.append(no)

    #for value in inputlist:
     #   print(value)

    filterresult=list(filter(Prime,inputlist))
    print("result after filter",filterresult)

    mapresult=list(map(conditionmap,filterresult))
    print("result after map",mapresult)

    reduceresult=reduce(reduceresult,mapresult)
    print("result after reduce",reduceresult)
    


if __name__=="__main__":
    main()