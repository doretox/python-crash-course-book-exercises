"""
3-5. Changing Guest List: You just heard that one of your guests can't make the dinnerso you need to send out a new set of invitations. You'll have to think of someone else to invite.
• Start with your program from Exercise 3-4.
Add a print statement at the end of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting .
• Print a second set of invitation messages, one for each person who is still in your list .
"""

guest_list = ['Elon Musk', 'Steve Jobs', 'Isaac Newton', 'Albert Einstein']

print("Hi, Mr. " + guest_list[0] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[1] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[2] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[3] + " would you like to join me for dinner?\n")

print("Mr. " + guest_list[3] + " can't make it.\n")

guest_list[3] = 'Nikola Tesla'

print("Hi, Mr. " + guest_list[0] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[1] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[2] + " would you like to join me for dinner?")
print("Hi, Mr. " + guest_list[3] + " would you like to join me for dinner?")

