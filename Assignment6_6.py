
def triangle(value):
    for i in range(1,value+1):
        print("\n")
        for j in range(1,i):
            print("*",end=" ")

def main():
    print("Enter number ")
    no=int(input())
    
    triangle(no)
   

if __name__=="__main__":
    main()