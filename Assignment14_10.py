class Employee:
    def __init__(self, A, B, C):
        self.Name = A           # public
        self._Department = B           # protected
        self.__Salary = C        # private
    
    def Display(self):
        print(self.Name)
        print(self._Department)
        print(self.__Salary)




class Derived(Employee):
    def __init__(self, A, B, C):
        super().__init__(A, B, C)




obj = Employee('Rahul',"comp",891212)
obj.Display()

print(obj.Name)
print(obj._Department)
#print(obj.__Salary)

