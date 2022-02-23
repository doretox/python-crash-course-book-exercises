"""
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
"""

magicians_names = ['Paul', 'Mark', 'Kurt', 'Maria', 'Pam']

def show_magicians(names):
    """Show all the magician's names."""
    print("\nThe Magicians names are: ")
    for name in names:
        print(name)

show_magicians(magicians_names)
