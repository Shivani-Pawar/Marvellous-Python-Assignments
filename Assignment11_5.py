count=0

def Countzero(value):
    global count
    if(value>0):
        i=value%10
        if(i==0):
            count=count+1
        
        value=int(value/10)
        Countzero(value)
    return count







def main():
    print("enter number")
    no=int(input())
    output=Countzero(no)
    print(output)




if __name__=="__main__":
    main()
