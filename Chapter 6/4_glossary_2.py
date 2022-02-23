"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary's keys and values.
When you're sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {
    'string': 'A sequence of characters.',
    'variable': 'Is a reserved memory location to store values.',
    'list': 'Is a collection of arbitrary objects.',
    'tuple': 'Is exactly like a list but its immutable.',
    'print': 'A function that prints a specified message in the screen.',
    'boolean expression': 'An expression that evaluates to True or False.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'float': 'A numerical value with a decimal component.',
} 

for key, value in glossary.items():
    print(key.title() + ": "+ value + "\n")

