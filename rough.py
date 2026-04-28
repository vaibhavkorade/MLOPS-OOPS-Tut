from project import chatbook

# #create list of numbers
# numbers = [1, 2, 3, 4, 5]

# #print addtion of all the numbers in the list
# total = sum(numbers)
# print(f"The total of the numbers in the list is: {total}")  # Output: The total of the numbers in the list is: 15

# #declare string variable
# name = "samuel"
# #declare integer variable
# age = 20

# print(type(numbers))  # Output: <class 'list'>
# print(type(name))     # Output: <class 'str'>
# print(type(age))      # Output: <class 'int'>

# numbers.append(6)  # Adding a new number to the list
# print(name.capitalize())  # Capitalizing the name string
# print(numbers)  # Output: [6]
# print(name)     # Output: Samuel

# #add two numbers
# num1 = 10
# num2 = 20
# result = num1 + num2
# print(f"The result of adding {num1} and {num2} is: {result}")  # Output: The result of adding 10 and 20 is: 30


# #add two strings
# str1 = "Hello, "
# str2 = "world!"
# result_str = str1 + str2
# print(f"The result of adding '{str1}' and '{str2}' is: '{result_str}'")  # Output: The result of adding 'Hello, ' and 'world!' is: 'Hello, world!'

chatbook_app = chatbook()
print(chatbook_app.id)  # Output: 1

chatbook_app1 = chatbook()
print(chatbook_app1.id)  # Output: 2

chatbook.set_private_variable_static(100)  # Setting the private variable using the static method
chatbook_app2 = chatbook()
print(chatbook_app2.id)  # Output: 101
