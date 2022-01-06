class Restaurant():
    """A class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("The restaurant is open.")
    
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("Welcome, the " + self.restaurant_name.title() +  " restaurant our speciality are " + self.cuisine_type.title() + ".")