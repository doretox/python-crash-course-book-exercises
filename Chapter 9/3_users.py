# 9-3. Users: Make a class called User. Create two attributes called #first_name and last_name, and then create several other attributes that are # typically stored in a user profile. Make a method called describe_user() #that prints a summary of the user’s information. Make another method called # greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

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

    
#creating instances
mark = User('mark', 'ross', 'mross', 'miker@email.com', 'new york')
paul = User('paul', 'stanley', 'pauls', 'paulst@email.com', 'montana')
gloria = User('gloria', 'smith', 'glorias', 'gsmith@email.com', 'denver')

#calling methods
mark.greet_user()
mark.describe_user()

paul.greet_user()
paul.describe_user()

gloria.greet_user()
gloria.describe_user()
