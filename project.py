#create class name chatbook
class chatbook:
    def __init__(self):
        print("Chatbook class constructor called")
        self.name = "Chatbook"
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def login(self, username, password):
        # Simulate login logic (for demonstration purposes)
        if username == "user" and password == "pass":
            self.logged_in = True
            print(f"Login successful for user: {username}")
        else:
            print("Login failed. Invalid username or password.")

    def menu(self):
        user_input = input("""Welcome to Chatbook! Please enter your username: 
                          1. Press 1 to signup
                          2. Press 2 to login
                          3. Press 3 to write a post
                          4. Press 4 to view posts
                          5. Press 5 to logout
                          """)

        if user_input == "1":
            self.signup()
        elif user_input == "2":           
            self.login()
        elif user_input == "3":
           pass  # Write post functionality is not implemented yet.
        elif user_input == "4":
           pass  # View posts functionality is not implemented yet.
        elif user_input == "5":
            pass  # Logout functionality is not implemented yet.
        else:
            print("Invalid input. Please try again.")
            exit()

        self.menu()  # Call the menu method again to allow continuous interaction until the user decides to exit.

    #create a method for signup
    def signup(self):
        # Simulate signup logic (for demonstration purposes)
        username = input("Enter your email id: ")
        password = input("Enter your password: ")
        self.username = username
        self.password = password        
        print(f"Signup successful for user: {username}")

    #create a method for login
    def login(self):
        # Simulate login logic (for demonstration purposes)
        if self.username == "" or self.password == "":
            print("No user registered. Please signup first by pressing 1.")
        else:            
            username = input("Enter your email id / username: ")
            password = input("Enter your password: ")
        if username == self.username and password == self.password:
            self.logged_in = True
            print(f"Login successful for user: {username}")
        else:
            print("Login failed. Invalid email id or password.")       
    

#cretae an object of the chatbook class 
chatbook_app = chatbook()     
#call the menu method to display the menu options
chatbook_app.menu() 
