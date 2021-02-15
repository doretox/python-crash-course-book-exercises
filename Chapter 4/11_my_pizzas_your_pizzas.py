# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •Add a new pizza to the original list.
# •Add a different pizza to the list friend_pizzas.
# •Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['pepperoni', 'margherita', 'bacon']

#copping the list
friend_pizzas = pizzas[:]

#adding a new flavor to the original list
pizzas.append('cheese')

#adding a new flavor to the friend's list
friend_pizzas.append('hawaiian')

print("My favorite pizzas are: " + str(pizzas) + "\n")

print("My friend's favorite pizzas are: " + str(friend_pizzas) + "\n")


