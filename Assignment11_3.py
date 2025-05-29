sum=0
def SumX(value):
    global sum
    if(value>0):
        i=value%10
        sum=sum+i
        
        value=int(value/10)
        SumX(value)
    return sum







def main():
    print("enter number")
    no=int(input())
    output=SumX(no)
    print(output)




if __name__=="__main__":
    main()
