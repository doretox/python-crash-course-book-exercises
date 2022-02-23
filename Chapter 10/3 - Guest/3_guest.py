"""
10-3. Guest: Write a program that prompts the user for their name. When they 
respond, write their name to a file called guest.txt.
"""

filename = 'guest.txt'

print("What's your name? ")
name = str(input(("> ")))

with open(filename, 'w') as file_object:
    file_object.write(name)