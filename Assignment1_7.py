def Divisiblebyfive(Value):
    if Value % 5==0:
        print("Divisible by 5")

    else:
        print("Not Divisible by 5")


def main():
    print("enter number")
    no=int(input())
    Divisiblebyfive(no)

if __name__=="__main__":
    main()