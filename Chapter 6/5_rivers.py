"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•Use a loop to print the name of each river included in the dictionary.
•Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

print("\n")

print("These rivers are included in the dictionary: ")
for key in rivers.keys():
    print("- " + key.title())

print("\n")

print("These countries are included in the dictionary: ")
for value in rivers.values():
    print("- " + value.title())

