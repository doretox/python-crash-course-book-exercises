"""
10-12. Favorite Number Remembered: Combine the two programs from 
Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it in a file. Run the program twice to see that it works.
"""
import json

# Load the favorite number, if it has been stored previously.
# Otherwise, prompt for the favorite number and store it.

filename = 'favotire_number.json'

try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    print("What's your favorite number?")
    favorite_number = input("> ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print(f"We'll remember your favorite number: {favorite_number}.")
else:
        print(f"We remember your favorite number. It is {favorite_number}.")