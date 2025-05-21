

double=lambda value:value+value



def main():
   print("enter number")
   no=int(input())
   s=[]
   print("enter numbers")
   for i in range(no):
       inpu=int(input())
       s.append(inpu)
   print(s)


   mdata=list(map(double,s))
   print(mdata)
   


if __name__=="__main__":
    main()