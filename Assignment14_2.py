class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.Width=b
        

    def Area(self):
        Area=self.length*self.Width
        print("Area of rectange is",Area)

    def Perimeter(self):
        Peri=2*(self.length+self.Width)
        print("perimeter of rectangle",Peri)


def main():
    print("enter length of rectange")
    l=int(input())

    print("enter width of rectangle")
    b=int(input())



    obj=Rectangle(l,b)
    obj.Area()
    obj.Perimeter()
    


if __name__=="__main__":
    main()