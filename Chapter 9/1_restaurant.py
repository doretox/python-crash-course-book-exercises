# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

from types import coroutine


class Restaurant():
    """A class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("Welcome, the " + self.restaurant_name.title() +  " restaurant is open and our speciality are " + self.cuisine_type.title() + ".")

my_restaurant = Restaurant('tabasco', 'burgers')

my_restaurant.open_restaurant()