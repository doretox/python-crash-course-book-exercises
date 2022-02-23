"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person1 = {
    'first_name': 'mark',
    'last_name': 'smith',
    'age': 32,
    'city': 'austin',
}

person2 = {
     'first_name': 'karen',
    'last_name': 'brown',
    'age': 28,
    'city': 'miami',
}

person3 = {
     'first_name': 'john',
    'last_name': 'baker',
    'age': 37,
    'city': 'chicago',
}

people = [person1, person2, person3]

for person in people:
    print("Name: " + person['first_name'].title() + " "
     + person['last_name'].title())
    print("Age: " + str(person['age']))
    print("City: " + person['city'].title() + "\n")
