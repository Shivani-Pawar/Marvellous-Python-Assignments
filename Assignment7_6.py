

def prime(value):
    count=0
    for i in range(2,value):
        if(value%i==0):
           count=count+1
    if count==0:

        return value



def main():
   print("enter number")
   no=int(input())
   s=[]
   print("enter numbers")
   for i in range(no):
       inpu=int(input())
       s.append(inpu)
   print(s)


   fdata=list(filter(prime,s))
   print(fdata)
   


if __name__=="__main__":
    main()