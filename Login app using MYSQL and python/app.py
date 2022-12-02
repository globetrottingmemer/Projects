import sys
from dbhelper import DBhelper

class Flipkart:

    def __init__(self):
        #Since menu will open we should connect to the databse here
        self.db = DBhelper()
        self.menu()


    def menu(self):

        user_input = input(""""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anthing else to leave
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)


    def register(self):
        name = input("Enter the name: ")
        email = input("Enter Email: ")
        password = input("Enter password: ")

        response = self.db.register(name, email, password)

        if response:
            print("Registration successful")
        else:
            print("Registration failed!!!")
        self.menu()

    def login(self):
        email = input("Enter your Email: ")
        password = input("Enter your passowrd: ")

        data = self.db.search(email, password)
        if len(data) == 0:
            print("""Login Failed!!!
Please enter correct Email\Password!!!""")
            self.login()
        else:
            print(" Login successful! Hello, ", data[0][1])
        self.login_menu()


    def login_menu(self):
        input("""" 
        1. enter 1 to see profile
        2. enter 2 to edit profile
        3. enter 3 to delete profile
        4. enter 4 to logout
        """)






obj = Flipkart()
