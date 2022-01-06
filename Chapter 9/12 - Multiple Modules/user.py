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