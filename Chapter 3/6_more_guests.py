"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
•Start with your program from Exercise 3-4 or Exercise 3-5. 
Add a print statement to the end of your program informing people that you found a bigger dinner table .
•Use insert() to add one new guest to the beginning of your list.
•Use insert() to add one new guest to the middle of your list.
•Use append() to add one new guest to the end of your list.
•Print a new set of invitation messages, one for each person in your list.
"""

guest_list = ['Elon Musk', 'Steve Jobs', 'Isaac Newton', 'Nikola Tesla']


print("Mrs " + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + "and" + guest_list[3] + " we found a bigger table.\n")

#Adding new guests
guest_list.insert(0, 'Richard Feynman')
guest_list.insert(3, 'Alan Turing')
guest_list.append('Leonardo da Vinci')

#Inviting to dinner
print("Hello Mr. " + guest_list[0] + " would you like to join me for dinner?")
print("Hello Mr. " + guest_list[3] + " would you like to join me for dinner?")
print("Hello Mr. " + guest_list[6] + " would you like to join me for dinner?")