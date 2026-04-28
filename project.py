#create class name chatbook
class chatbook:
    def __init__(self):
        print("Chatbook class constructor called")
        self.name = "Chatbook"
        self.username = ""
        self.password = ""
        self.logged_in = False

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
            print("Signup functionality is not implemented yet.")
        elif user_input == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.login(username, password)
        elif user_input == "3":
            if self.logged_in:
                print("Write a post functionality is not implemented yet.")
            else:
                print("Please login to write a post.")
        elif user_input == "4":
            print("View posts functionality is not implemented yet.")
        elif user_input == "5":
            if self.logged_in:
                self.logged_in = False
                print("You have been logged out.")
            else:
                print("You are not logged in.")

#cretae an object of the chatbook class
chatbook_app = chatbook()                