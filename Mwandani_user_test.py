from main import Mwandani_user


data_store = []
class create_create_a_user_account:
  
    def __init__(self):
        self.firstname = 'john'
        self.middlename = 'doe'
        self.username = 'johndoe'
        self.password = '@john'    
        return Mwandani_user(self.firstname, self.middlename,self.username, self.password)
  
class register_a_user_in_the_data_store:
  
    def __init__(self):
        user = Mwandani_user('jane','doe','janedoe','smith&doe')
        return data_store.append(user)
  

  