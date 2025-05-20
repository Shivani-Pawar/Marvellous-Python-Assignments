def periofrect(l,b):
    p=(l+b)*2
    return p

def Areaofrect(l,b):
    a=l*b
    return a

def main():
    print("Enter length of rectange")
    length=int(input())

    print("Enter width of rectange")
    width=int(input())
    
    a=Areaofrect(length,width)
    print("the area is ",a)

    p=periofrect(length,width)
    print("the perimeter is",p)

if __name__=="__main__":
    main()