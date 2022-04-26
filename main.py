""" Password Locker Application. """
# Dependencies for generating random passwords
import string
import random

# APPLICATION HEADER

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

# DATA STRUCTURES FOR STORING OBJECTS

mwandani_app_store = []
mwandani_user_store = []

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def new_random_password(apps_name):
    """Returns a new randomly generated password. Takes password length as input."""

    pwd_length = int(input("Please enter the password length: "))
    random.shuffle(characters)
    password = []

    for i in range(pwd_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    new_password = "".join(password)
    print(f"{apps_name}'s new password is {new_password}")

    return new_password


def createPassword(app_name, option):
    """Decides whether to outsource password creation to password generator function."""

    if option == 2:
        return new_random_password(app_name)
    else:
        return


class Application:
    """Creates application objects with app name and password to later be stored in a list."""

    def __init__(self, name, password):
        self.app = {
            'app_name': name,
            'app_password': password
        }

    def register_app(self):
        mwandani_app_store.append(self.app)


class Mwandani_user:
    """Creates user objects. Main program takes in credentials then instantiates a Mwandani_user class."""

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
        if login_name == self.user['user_name'] and login_password == self.user['password']:
            return True
        else:
            return False

# BUSINESS LOGIC

running = True

while running:
    program_active = input("PRESS 'y' TO PROCEED OR TYPE 'quit' TO EXIT APPLICATION: ")

    if program_active.lower() == 'quit' or program_active == 'q':
        print("\nWe're sad to see you go :-( Catch you later though.\n")
        running = False
        break

    if program_active.lower() == 'y' or program_active.lower() == 'yes':
        print("\nHi, Kindly select an option number to proceed: ")
        print("""
        1. Signup on Mwandani
        2. Sign into your Mwandani Account
        3. Manage your Mwandani Account [COMING SOON]
        4. Forgotten Password? [COMING SOON]

        """)

        navigation_option = int(input(": "))

        # Above options are mutually exclusive so if a user signups and creates an object in one option
        # the logic will continue to work only if he does os again in new option
        # improve: Make more DRY

        if navigation_option == 1:
            print("To signup on Mwandani, kindly enter ...")
            first_name = input("Your First Name: ")
            middle_name = input("Your Middle Name: ")
            username = input("Please enter a unique Mwandani Username: ")
            password = input("Please enter a new Mwandani Password: ")
            print("\n--------------------------------------------------")
            print("\t\t\o/ Success you now have a Mwandani account\t\t")
            print("--------------------------------------------------\n")

            current_user = Mwandani_user(first_name, middle_name, username, password)
            current_user.register_user()

            verify_account = input("Proceed to Log into my account?(y/n): ")
            if verify_account.lower() == 'n':
                break
            else:
                pass
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            my_user_name = input("Enter your username: ")
            my_password = input("Enter your password: ")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            while True:
                if current_user.login_user(my_user_name, my_password):
                    print(f" \o/ Success: You're now logged in as {my_user_name}")
                    break
                else:
                    print(":( Sorry: The details you entered don't match with our records")
                    print("Please try again. Or type 'q' to exit.")

        if navigation_option == 2:

            while True:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                my_user_name = input("Enter your username: ")
                my_password = input("Enter your password: ")
                verify_account = input("Proceed to Log me in?(y/n): ")

                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if verify_account.lower() == 'y':
                    break
                else:
                    continue

                # because we can't persist data - we'll have to create a new object when a user logins as well
            print(f"[Logged in as {my_user_name}]")
            print("\nKindly select an option number to proceed:")
            print("""
            1. Register new app
            2. Retrieve credentials (single app)
            3. Retrieve all app's credentials 
            4. Delete credentials                  

            """)
            sign_in_step = int(input(": "))

            if sign_in_step == 1:
                while True:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    user_app_name = (input("Please enter application's name: ")).lower()
                    print(f"{user_app_name}'s Password Options: \n1. Enter Own Password \n2. Suggest a password for me")
                    user_password_option = int(input("\n1 or 2: "))

                    if user_password_option == 1:
                        user_app_password = input("Enter application's password: ")
                    if user_password_option == 2:
                        user_app_password = createPassword(user_app_name, user_password_option)

                    new_app = Application(user_app_name, user_app_password)
                    new_app.register_app()

                    registration = input("\nRegister another app? (y/n): ")
                    if registration.lower() == 'y':
                        continue
                    if registration.lower() == 'n':
                        break

            if sign_in_step == 2:
                user_app_name = (input("Type the app's name and press ENTER to proceed: ")).lower()

                for app in mwandani_app_store:
                    if app['app_name'] == user_app_name:
                        print("_______________________________________________________________________________________")
                        print(f"\t\t\t{app['app_name']} : {app['app_password']} ")
                        print("_______________________________________________________________________________________")

            if sign_in_step == 3:
                for app in mwandani_app_store:
                    print("___________________________________________________________________________________________")
                    print(f"\t\t\tUsername: {app['app_name']}  Password: {app['app_password']}")
                    print("___________________________________________________________________________________________")

            if sign_in_step == 4:
                user_app_name = input("Type the app's name and press ENTER to delete [X]: ")

                # Range set once with initial length thus need to break after deletion else error 4 nxt iteration.
                for i in range(len(mwandani_app_store)):
                    if mwandani_app_store[i]['app_name'] == user_app_name:
                        del mwandani_app_store[i]
                        print(f"\o/{user_app_name} has been deleted successfuly.")
                        break  # the next iteration will contain the initial number of lists not the length of lists - 1

            else:
                pass

        if navigation_option == 3:
            print("manage users account")
            print("Coming soon: Allows you to update your mwandani username and password")

        if navigation_option == 4:
            print("user password recovery")
            print("Coming soon: Allows you to set password hint, recover forgotten passwords etc.")

    else:
        print("!Kindly enter either 'quit' or 'y'")

print("@)- Thank you for choosing Mwandani \n \t\t We got your back.")


















