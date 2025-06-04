class Student:
    School_name="carmel"
    def __init__(self,n,r):
        self.name=n
        self.roll_no=r
        
        

    def Display(self):
        print("School name is",Student.School_name)
        print("name of student",self.name)
        print("Roll number of student",self.roll_no)
        




def main():
    print("name of student")
    name=input()
    print("roll number of student")
    roll=int(input())
    obj=Student(name,roll)
    obj.Display()
    Student.School_name="Sacred heart"
    obj.Display()
    



if __name__=="__main__":
    main()