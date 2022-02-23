"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians' names. Because the
original list will be unchanged, return the new list and store it in a separate
list. Call show_magicians() with each list to show that you have one list
of the original names and one list with the Great added to each magician's name.
"""

def show_magicians(names):
    """ Print the name of each great magician."""
    for name in names:
        print(name)

def make_great(magicians):
    """ Add 'the great' to each magician name."""

    # making an empty list
    great_magicians = []

    # adding the great
    while magicians:
        magician = magicians.pop()
        great_magician = 'The Great ' + magician
        great_magicians.append(great_magician)

    # Add to the original list
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians_names = ['Paul', 'Mark', 'Kurt', 'Maria', 'Pam']

print("\nGreat magicians:")
great_magicians = make_great(magicians_names[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians_names)