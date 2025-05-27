
from functools import reduce

condition1=lambda no:no>=70 and no<=90
condition2=lambda no:no+10
condition3=lambda no1,no2:no1*no2

def main():
    print("enter size")
    size=int(input())
    
    print("enter number in list")
    inputlist=[]
    for i in range(size):
        no=int(input())
        inputlist.append(no)

    for value in inputlist:
        print(value)

    filterresult=list(filter(condition1,inputlist))
    print("result after filter",filterresult)

    mapresult=list(map(condition2,filterresult))
    print("the result for map is",mapresult)


    reduceresult=reduce(condition3,mapresult)
    print("the reduce result",reduceresult)    


if __name__=="__main__":
    main()