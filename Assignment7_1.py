

square=lambda value:value**2

cube=lambda value2:value2**3

def main():
   print("enter number")
   no=int(input())
   s=square(no)
   print(s)
   
   c=cube(no)
   print(c)


if __name__=="__main__":
    main()