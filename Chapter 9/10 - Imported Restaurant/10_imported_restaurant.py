"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a  module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
"""

import restaurant

new_restaurant = restaurant.Restaurant('Don Pepe', 'Pizza')

new_restaurant.open_restaurant()
new_restaurant.describe_restaurant()