"""
3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests .
•Start with your program from Exercise 3-6 . 
Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they're still invited.
•Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.
"""

guest_list = ['Richard Feynman', 'Elon Musk', 'Steve Jobs', 'Alan Turing', 'Isaac Newton', 'Nikola Tesla', 'Leonardo da Vinci']

print("My new table won't arrive at time so I can invite only two people for my dinner.\n")

#Popping guests
guest_popped = guest_list.pop(0)
print("Sorry Mr. " + guest_popped + " I can't invite you to dinner anymore.\n")
guest_popped = guest_list.pop(1)
print("Sorry Mr. " + guest_popped + " I can't invite you to dinner anymore.\n")
guest_popped = guest_list.pop(1)
print("Sorry Mr. " + guest_popped + " I can't invite you to dinner anymore.\n")
guest_popped = guest_list.pop(1)
print("Sorry Mr. " + guest_popped + " I can't invite you to dinner anymore.\n")
guest_popped = guest_list.pop(1)
print("Sorry Mr. " + guest_popped + " I can't invite you to dinner anymore.\n")
print("Mr. " + guest_list[0] + " and " + guest_list[1] + " you're still invited for my dinner.")

#Empty the list
del(guest_list[0])
del(guest_list[0])

#Print empty list.
print(guest_list)

