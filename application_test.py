from main import Application

data_store = []
class create_application_credentials:  
  
    def __init__(self):
        self.name = 'an_application_name'
        self.password = 'an_application_password'    
        return Application(self.name, self.password)
  
class register_application_in_data_store:

    def __init__(self):
      app = Application('the_app','its_password')
      return data_store.append(app)
    