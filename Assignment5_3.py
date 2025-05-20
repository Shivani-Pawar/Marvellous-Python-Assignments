
def CheckEligibility(age):
    if age>=18:
        print("Eligible to vote")
    else:
        print("not Eligible to vote")

def main():
    print("Enter age")
    a=int(input())
    CheckEligibility(a)

if __name__=="__main__":
    main()