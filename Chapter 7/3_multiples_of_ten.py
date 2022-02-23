"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""

number = input("Enter a number and I'll check if it is a multiple of 10: ")

#making the number a int
number = int(number)

#checking if it is multiple of 10
if number % 10 == 0:
    print("Nice! Your number is a multiple of 10.")
else:
    print("Your number isn't a multiple of 10.")