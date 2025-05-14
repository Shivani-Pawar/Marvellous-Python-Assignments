def Star(Value):
    for i in range(1,Value+1,1):
        print("\n")

        for j in range(1,Value+1,1):
            print("*",end=" ")




def main():
    print("Enter number")
    no1=int(input())
    Star(no1)

    


if __name__=="__main__":
    main()