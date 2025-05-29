
def Display(value):
    if(value>=1):
        print(value)
        value=value-1
        Display(value)




def main():
    print("enter number")
    no=int(input())
    Display(no)




if __name__=="__main__":
    main()
