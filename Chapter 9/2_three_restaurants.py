#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

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
        print("Welcome, the " + self.restaurant_name.title() +  " restaurant our speciality are " + self.cuisine_type.title() + ".\n")

#creating instances
restaurant_1 = Restaurant('bobs', 'burgers')
restaurant_2 = Restaurant('spoletto', 'pasta')
restaurant_3 = Restaurant('pizza hut', 'pizza')

#calling the methods
restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()

restaurant_2.open_restaurant()
restaurant_2.describe_restaurant()

restaurant_3.open_restaurant()
restaurant_3.describe_restaurant()

