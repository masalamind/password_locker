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

running = True

while running:

    program_active = input("Press Y to proceed or Type 'quit' to exit: ")

    if program_active.lower() == 'quit' or program_active == 'q':
        print("\nWe're sad to see you go :-(. Catch you later though.\n")
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
            print("signup the user")
        if navigation_option == 2:
            print("sign in the user")
        if navigation_option == 3:
            print("manage users account")
        if navigation_option == 4:
            print("user password recovery")

    else:
            print("!Kindly enter either 'quit' or 'y'")

print(":-) Thank you for choosing Mwandani. We got your back.")


# DATA STRUCTURES







