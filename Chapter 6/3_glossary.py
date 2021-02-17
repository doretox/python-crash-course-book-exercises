# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary .
# However, to avoid confusion, let’s call it a glossary.
# •Think of five programming words you’ve learned about in the previous
# chapters . Use these words as the keys in your glossary, and store their 
# meanings as values.
# •Print each word and its meaning as neatly formatted output . You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line . Use the 
# newline character (\n) to insert a blank line between each word-meaning 
# pair in your output . 

glossary = {
    'string': 'is a sequence of characters.',
    'variable': 'is a reserved memory location to store values.',
    'list': 'is a collection of arbitrary objects.',
    'tuple': 'is exactly like a list but its immutable.',
    'print': 'is a function that prints a specified message to the screen',
}

print("A string in Python " + str(glossary['string']) + "\n")

print("A variable in Python " + str(glossary['variable']) + "\n")

print("A list in Python " + str(glossary['list']) + "\n")

print("A tuple in Python " + str(glossary['tuple']) + "\n")

print("A print in Python " + str(glossary['print']) + "\n")