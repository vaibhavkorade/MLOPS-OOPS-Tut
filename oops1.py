from project import chatbook

#create new class employee
class employee :
    def __init__(self):
        print("Employee class constructor called")
        self.name = "Samuel"
        self.age = 20
        self.salary = 50000
        self.designation = "Software Engineer"
        print("Employee class constructor executed")
        print(id(self))  # Print the memory address of the object

    def display(self, destination):
        print("Employee details called manually:")
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Designation: {self.designation}")
        print(f"Destination: {destination}")
    
    #method to access chtbook menu
    def access_chatbook_menu(self):
        chatbook_app = chatbook()     
        print(chatbook_app.__variable)  

# #create an object of the employee class
# emp1 = employee()
# emp1.id = 12345  # Adding an id attribute to emp1
# print(id(emp1))  # Print the memory address of emp1 to confirm it's the same as printed in the constructor
# print(emp1.id)  # Output: 12345

# emp2 = employee()  # Create another object to show that it has a different memory address
# print(id(emp2))  # Print the memory address of emp2 to confirm it's different from emp1
# #access the attributes of the employee object
# emp1.display("kerala")  # Output: Name: Samuel, Age: 20, Salary: 50000, Designation: Software Engineer

emp1 = employee()
emp1.access_chatbook_menu()