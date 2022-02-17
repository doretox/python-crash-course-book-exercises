"""
10-11. Favorite Number: Write a program that prompts for the user's favorite 
number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite 
number! It's _____.”
"""
import json

print("What's your favorite number?")
favorite_number = input("> ")

filename = 'favorite_number.json'

with open (filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
