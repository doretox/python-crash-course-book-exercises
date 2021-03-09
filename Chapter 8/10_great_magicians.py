# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by
# adding the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.

magicians_names = ['Paul', 'Mark', 'Kurt', 'Maria', 'Pam']

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
        magicians_names.append(great_magician)


print("The name of the magicians are: ")
make_great(magicians_names)
show_magicians(magicians_names)