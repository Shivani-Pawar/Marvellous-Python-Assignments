mul=1
def Power(value,pow):
    global mul
    if(pow>=1):
        
        mul=mul*value
        
        
        pow=pow-1
        Power(value,pow)
    return mul







def main():
    print("enter number")
    no=int(input())
    print("enter power")
    p=int(input())
    output=Power(no,p)
    print(output)




if __name__=="__main__":
    main()
