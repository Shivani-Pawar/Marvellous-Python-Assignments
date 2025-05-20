
def Largest(value1,value2,value3):
    if (value1>value2 and value1>value3):
        print("larget number is",value1)
    elif(value2>value1 and value2>value3):
        print("larget number is",value2)
    elif(value3>value1 and value3>value2):
        print("larget number is ",value3)

def main():
    print("Enter first number")
    no1=int(input())
    print("enter second number")
    no2=int(input())
    print("enter third number")
    no3=int(input())
    Largest(no1,no2,no3)

if __name__=="__main__":
    main()