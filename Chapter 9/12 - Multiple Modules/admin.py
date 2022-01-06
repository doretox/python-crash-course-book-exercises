from user import User

class Admin(User):
    """A class to model a admin user."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """Print user's privileges."""
        print("The user " + self.username + " has the following privileges: " + str(self.privileges))