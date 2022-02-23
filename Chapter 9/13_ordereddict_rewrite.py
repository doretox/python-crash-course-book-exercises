"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you 
used a standard dictionary to represent a glossary. Rewrite the program using 
the OrderedDict class and make sure the order of the output matches the order 
in which key-value pairs were added to the dictionary.
"""

from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A sequence of characters.'
glossary['variable'] = 'Is a reserved memory location to store values.'
glossary['list'] = 'Is a collection of arbitrary objects.'
glossary['tuple'] = 'Is exactly like a list but its immutable.'
glossary['print'] = 'A function that prints a specified message in the screen.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['float'] = 'A numerical value with a decimal component.'

for key, value in glossary.items():
    print(key.title() + ": "+ value + "\n")