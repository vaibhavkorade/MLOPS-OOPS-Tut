class employee :
    def __init__(self):
        print("Employee class constructor called")
        self.name = "Samuel"
        self.age = 20
        self.salary = 50000
        self.designation = "Software Engineer"
        print("Employee class constructor executed")

    def display(self):
        print("Employee details called manually:")
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Designation: {self.designation}")

#create an object of the employee class
emp1 = employee()

#access the attributes of the employee object

# print(emp1.name)  # Output: Samuel
# print(emp1.age)   # Output: 20  
# print(emp1.salary)  # Output: 50000
# print(emp1.designation)  # Output: Software Engineer

#or we can use the display method to print all the details of the employee
emp1.display()  # Output: Name: Samuel, Age: 20, Salary: 50000, Designation: Software Engineer  

print( type(emp1) )  # Output: <class '__main__.employee'>