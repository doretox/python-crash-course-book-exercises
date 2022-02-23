"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""

class User():
    """A class to descrite a generic user."""
    
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize users infos."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.locaiton = location.title()

    def greet_user(self):
        """Display a message to greet the user."""
        print("Welcome " + self.first_name + self.last_name + "!")
        print("Here are your data\n")
        
    def describe_user(self):
        """Display a summary of the user's information."""
        print("Name: " + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.locaiton + "\n")

class Admin(User):
    """A class to model a admin user."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()
       
class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        """Print user's privileges."""
        print("The user has the following privileges: " + str(self.privileges))

john = Admin('john', 'snow', 'jnow', 'jsnow@email.com', 'california')
john.privileges.show_privileges()

print("\nAdding privileges...")
john_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

john.privileges.privileges = john_privileges
john.privileges.show_privileges()