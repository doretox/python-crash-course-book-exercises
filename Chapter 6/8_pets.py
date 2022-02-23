"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.
"""

# Empty list to store pets
pets = []

# individual pets and store in the list
ollie = {
    'name': 'ollie',
    'type': 'dog',
    'owner': 'mark',
    'weight': '5kg',
    'age': '7 y',
}
pets.append(ollie)

jack = {
    'name': 'jack',
    'type': 'cat',
    'owner': 'maria',
    'weight': '2kg',
    'age': '3 y',
}
pets.append(jack)

lola = {
    'name': 'lola',
    'type': 'turtle',
    'owner': 'marie',
    'weight': '300g',
    'age': '1 y',
}
pets.append(lola)

lucy = {
    'name': 'lucy',
    'type': 'hamster',
    'owner': 'john',
    'weight': '200g',
    'age': '4 y',
}
pets.append(lucy)

for pet in pets:
    print("Pet name: " + pet['name'].title())
    print("Type: " + pet['type'].title())
    print("Owner: " + pet['owner'].title())
    print("Weight: " + str(pet['weight']))
    print("Pet age: " + str(pet['age'] + "\n"))
