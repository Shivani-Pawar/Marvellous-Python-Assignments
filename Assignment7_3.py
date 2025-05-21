

even=lambda value:value%2==0



def main():
   print("enter number")
   no=int(input())
   s=[]
   print("enter numbers")
   for i in range(no):
       inpu=int(input())
       s.append(inpu)
   print(s)


   fdata=list(filter(even,s))
   print(fdata)
   


if __name__=="__main__":
    main()