class Employee:
    def __init__(self,N,id,Sal):
        self.Name=N
        self.emp_id=id
        self.Salary=Sal

    def Display(self):
        print("name of employee is",self.Name)
        print("Salary of employee is",self.Salary)
        print("Employee id is",self.emp_id)


def main():
    print("enter name of employee")
    name=input()

    print("enter id of employee")
    id=int(input())


    print("enter salry of employee")
    s=int(input())

    obj=Employee(name,id,s)
    obj.Display()


if __name__=="__main__":
    main()