"""
9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
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
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """Print user's privileges."""
        print("The user " + self.username + " has the following privileges: " + str(self.privileges))

jax = Admin('jax', 'teller', 'jteller', 'jteller@email.com', 'charming')
jax.show_privileges()