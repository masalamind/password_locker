mwandani_app_store = [{'app_name': 'fb', 'app_password': 'blue'},
                      {'app_name': 'gmail', 'app_password': 'red'},
                      {'app_name': 'ig', 'app_password': 'purple'}]

user_app_name = input("Enter the app's name: ")

# the range is set only once with initial list length thus we need to break less you get an out of index error
for i in range(len(mwandani_app_store)):

    if mwandani_app_store[i]['app_name'] == user_app_name:
        del mwandani_app_store[i]


        print(f"{user_app_name} has been deleted successfuly.")
        break; # the next iteration will contain the initial number of lists not the no of lists - 1

print(mwandani_app_store)
#
# for i in range (len(mwandani_app_store)):
#     print(mwandani_app_store[i])
#     if app['app_name'] == user_app_name:
#         print(app['app_password'])