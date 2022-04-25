""" Password Locker Application. """

# NAVIGATION UI

print("\n")
print("""-----------------------------------------------------------------------------------------------------------""")
print("""\n                                        WELCOME TO MWANDANI !                                            """)

print("""            
                        Generate, Store, & Manage Your Online Passwords Offline 

                            * Say goodbye to  forgetting your passwords 
                            * No more using the same password everywhere
                            * Adios to guessing unique passwords all by yourself 
""")
print("""-----------------------------------------------------------------------------------------------------------""")
print("\n")

# DATA STRUCTURES
mwandani_app_store = []
mwandani_user_store = []


class Application:

    def __init__(self, name, password):
        self.app = {
            'app_name': name,
            'app_password': password
        }

    def register_app(self):
        mwandani_app_store.append(self.app)


class Mwandani_user:

    def __init__(self, user_first_name, user_middle_name, user_username, user_password):
        self.user = {
            'first_name': user_first_name ,
            'middle_name': user_middle_name,
            'user_name': user_username,
            'password': user_password
        }

    def register_user(self):
        # Add new user object to list of Mwandani users
        mwandani_user_store.append(self.user)


    def login_user(self, login_name, login_password):
        if login_name == self.username and login_password == self.password:
            return True
        else:
            return False

# BUSINESS LOGIC


running = True

while running:


    program_active = input("Press Y to proceed or Type 'quit' to exit: ")

    if program_active.lower() == 'quit' or program_active == 'q':
        print("\nWe're sad to see you go :-( Catch you later though.\n")
        running = False
        break

    if program_active.lower() == 'y' or program_active.lower() == 'yes':
        print("\nSelect an option number to proceed: ")
        print("""
        1. Signup on Mwandani
        2. Sign into your Mwandani Account
        3. Manage your Mwandani Account
        4. Forgotten Password?

        """)

        navigation_option = int(input(": "))

        if navigation_option == 1:
            print("Hello, Kindly enter your")
            first_name = input("Your First Name: ")
            middle_name = input("Your Middle Name: ")
            username = input("Please enter a unique Mwandani Username: ")
            password = input("Please enter a new Mwandani Password: ")

            current_user = Mwandani_user(first_name, middle_name, username, password)
            current_user.register_user()



        if navigation_option == 2:

            # INSERT: Code to login

            print("\nKindly select an option number to proceed:")
            print("""
            1. Register a new app
            2. Retrieve app's credentials
            3. Retrieve all app's credentials                   

            """)
            sign_in_step = int(input(": "))

            if sign_in_step == 1:
                while True:
                    user_app_name = (input("Please enter application's name: ")).lower()
                    user_app_password = input("Enter application's password: ")
                    new_app = Application(user_app_name, user_app_password)
                    new_app.register_app()

                    registration = input("Register another app? (y/n): ")
                    if registration.lower() == 'y':
                        continue
                    if registration.lower() == 'n':
                        break


            elif sign_in_step == 2:
                user_app_name = (input("Please enter application's name: ")).lower()

            elif sign_in_step == 3:
                pass

            else:
                pass

        if navigation_option == 3:
            print("manage users account")
        if navigation_option == 4:
            print("user password recovery")

    else:
            print("!Kindly enter either 'quit' or 'y'")

for user in mwandani_user_store:
    print(user)
for app in mwandani_app_store:
    print(app)

print(":-) Thank you for choosing Mwandani. We got your back.")






    # def view_accounts(self):
    #     print("""
    #             1. Enter application name
    #             2. View all applications credentials
    #
    #             """)
    #     view_accounts_mode = int(input(": "))
    #
    #     if view_accounts_mode == 1:
    #         user_app_name = (input("Enter application name: ")).lower()
    #         user_pwd = input("Enter Mwandani Password: ")
    #         # if user_pwd == mwandani_user_db.self.username == user_pwd: # db stored as key value pairs usrnm: pwed
    #             # mwandani_app_db.query user
    #
    #
    #     elif view_accounts_mode == 2:
    #         user_pwd = input("Enter Mwandani Password: ")
    #         # Iterate all items in the mwandani_user_db
    #
    #     else:
    #         print("!Kindly enter either 1 or 2")
    #












