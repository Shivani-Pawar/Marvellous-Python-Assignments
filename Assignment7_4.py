from functools import reduce

product=lambda value1,value2:value1*value2



def main():
   print("enter number")
   no=int(input())
   s=[]
   print("enter numbers")
   for i in range(no):
       inpu=int(input())
       s.append(inpu)
   print(s)


   rdata=(reduce(product,s))
   print(rdata)
   


if __name__=="__main__":
    main()