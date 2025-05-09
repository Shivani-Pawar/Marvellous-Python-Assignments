def Displaystar(Value):
    for i in range(1,6,1):
        print("*",end=' ')

def main():
    print("enter number")
    no=int(input())
    Displaystar(no)


if __name__=="__main__":
    main()