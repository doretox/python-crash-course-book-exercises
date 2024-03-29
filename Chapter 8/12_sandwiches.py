"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
"""

def make_sandwich(*items):
    """Build a sandwich with different items in it."""
    print ("Making a sandwich with: ")
    for item in items:
        print("- " + item)


make_sandwich('peperoni')

print("\n")

make_sandwich('cheese', 'ham')

print("\n")

make_sandwich('chicken', 'lettuce', 'tomato')