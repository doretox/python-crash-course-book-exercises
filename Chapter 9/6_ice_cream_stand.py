#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. #Write a class called IceCreamStand that inherits from the Restaurant class #you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either #version of the class will work; just pick the one you like better. Add an #attribute called flavors that stores a list of ice cream flavors. Write a #method that displays these flavors. Create an instance of IceCreamStand, and #call this method.

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

class IceCreamStand(Restaurant):
    """A class to model a specific kind of restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class. Then initialize attributes specific to an Ice Cream Stand."""
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        """Prints the flavors."""
        print("The flavors avaliable are: " + str(self.flavors))

new_restaurant = IceCreamStand('Bobs', 'Fast Food')
new_restaurant.display_flavors()
        