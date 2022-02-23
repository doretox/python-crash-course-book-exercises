"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary .
"""

person = {
    'first_name': 'mark',
    'last_name': 'smith',
    'age': 32,
    'city': 'austin',
}

print("First name: " + str(person['first_name'].title()) + "\n")

print("Last name: " + str(person['last_name'].title()) + "\n")

print("Age: " + str(person['age']) + "\n")

print("City: " + str(person['city'].title()) + "\n")