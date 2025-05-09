def Add(Value1,Value2):
    result=Value1+Value2
    return result


def main():
    print("Enter number1")
    no1=int(input())


    print("Enter number2")
    no2=int(input())

    addition=Add(no1,no2)
    print("additon is", addition)

if __name__=="__main__":
    main()    