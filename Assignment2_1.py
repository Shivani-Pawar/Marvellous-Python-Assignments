from Arithematic import Add
from Arithematic import Sub
from Arithematic import Multi
from Arithematic import Div


def main():
    print("enter number 1")
    no1=int(input())
    print("enter second number")
    no2=int(input())
    addresult=Add(no1,no2)
    print("the result after addition",addresult)


    subresult=Sub(no1,no2)
    print("the result after substraction",subresult)

    Multiresult=Multi(no1,no2)
    print("the result after multiplication",Multiresult)

    Divresult=Div(no1,no2)
    print("the result after division",Divresult)
    


if __name__=="__main__":
    main()