"""
3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

languages = ['C', 'PHP', 'Java', 'Python', 'JavaScript', 'C++', 'Ruby', 'Perl']

#sorting the list
languages.sort()
print(languages)

#sorting reverse
languages.sort(reverse=True)
print(languages)

#sorting temporarily
print(sorted(languages))

#reverse order
languages.reverse()
print(languages)

#printing the length of the list 
print("The length of the list is: " + str(len(languages)) + " itens.")