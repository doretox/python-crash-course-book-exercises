"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person's
name along with their favorite numbers.
"""

favorite_numbers = {
    'john':  ['1', '10'],
    'karen': ['4', '14'],
    'joseph': ['4', '23', '32'],
}

for name, numbers in favorite_numbers.items():
        print(name.title() + "'s" + " favorite numbers are: ")
        for number in numbers:
            print(number)
        print("\n")