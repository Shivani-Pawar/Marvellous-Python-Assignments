def CheckNum(Value):
    if Value < 0:
        print("Negative Number")
    elif Value > 0:
        print("Positive Number")
    else:
        print("Zero")

def main():
    print("Enter number")
    no=int(input())
    CheckNum(no)

if __name__=="__main__":
    main()
