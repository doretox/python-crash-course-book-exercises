# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

pizzas = ['pepperoni', 'margherita', 'bacon']

#copping the list
friend_pizzas = pizzas[:]

#adding a new flavor to the original list
pizzas.append('cheese')

#adding a new flavor to the friend's list
friend_pizzas.append('hawaiian')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print("- " + pizza)

print("My friend's favorite pizza are: ")
for pizza in friend_pizzas:
    print("- " + pizza)