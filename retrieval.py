mwandani_app_store = [{'app_name': 'fb', 'app_password': 'blue'},
                      {'app_name': 'gmail', 'app_password': 'red'},
                      {'app_name': 'ig', 'app_password': 'purple'}]

user_app_name = input("Enter the app's name: ")
for app in mwandani_app_store:
    if app['app_name'] == user_app_name:
        print(app['app_password'])