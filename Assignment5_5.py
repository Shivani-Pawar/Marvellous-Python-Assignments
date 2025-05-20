
def Checkoddeven(value1):
    if (value1%2==0):
        print("The",value1,"is even number")
    else:
        print("The",value1,"is odd number")

def main():
    print("Enter first number")
    no1=int(input())
    
    Checkoddeven(no1)

if __name__=="__main__":
    main()