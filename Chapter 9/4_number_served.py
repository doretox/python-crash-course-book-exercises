# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers
# the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served. Call this method with a new number and 
# print the value again.
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, a day 
# of business.

class Restaurant():
    """A class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print("The restaurant is open.")
    
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("Welcome, the " + self.restaurant_name.title() +  " restaurant our speciality are " + self.cuisine_type.title() + ".")

    def read_customers_served(self):
        """Print a statment showing how many customers has been served."""
        print("This restaurant has served " + str(self.number_served) + " customers.")

    def set_number_served(self, number):
        """Set te number of costumers served to the given value."""
        self.number_served = number

    def increment_number_served(self, served_to_add):
        """Add the given amount to the costumers served value."""
        self.number_served += served_to_add

# First chore of the exercise
restaurant_1 = Restaurant('Burger King', 'burgers')
restaurant_1.read_customers_served()
restaurant_1.number_served = 10
restaurant_1.read_customers_served()

print("-------------------------------------------")

#Second chore
restaurant_2 = Restaurant('Pizza Hut', 'Pizza')
restaurant_2.set_number_served(23)
restaurant_2.read_customers_served()

print("-------------------------------------------")

#Third chore
restaurant_3 = Restaurant('KFC', 'Fried Chicken')
restaurant_3.set_number_served(32)
restaurant_3.read_customers_served()
restaurant_3.increment_number_served(10)
restaurant_3.read_customers_served()