# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User():
    """A class to descrite a generic user."""
    
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize users infos."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.locaiton = location.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the value of login_attempts to 0."""
        self.login_attempts = 0
    
    def print_login_attempts(self):
        """Prints the number of login attempts."""
        print("The user " + self.username + " tried to login " + str(self.login_attempts) + " times.")
    
        
# First chore
mark = User('mark', 'ross', 'mross', 'miker@email.com', 'new york')
mark.increment_login_attempts()
mark.print_login_attempts()
print("\n")

# increasing several times
mark.increment_login_attempts()
mark.increment_login_attempts()
mark.increment_login_attempts()
mark.increment_login_attempts()
mark.print_login_attempts()
print("\n")

#reseting the number of attempts
mark.reset_login_attempts()
mark.print_login_attempts()

