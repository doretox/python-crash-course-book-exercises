"""
9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the 
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Dice with one attribute called sides, which has a default 
value of 6. Write a method called roll_dice() that prints a random number 
between 1 and the number of sides the dice has. Make a 6-sided die and roll 
it 10 times.
Make a 10-sided dice and a 20-sided dice. Roll each die 10 times.
"""

from random import randint

class Dice():
    """A class to represent a Dice."""

    def __init__(self, sides=6):
        """Initialize the dice."""
        self.sides = sides

    def roll_dice(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)

#make a 6 side dice and roll it 10 times
d6 = Dice()
results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 rolls of a 6-sided dice:")
print(results)

#make a 10 side dice and roll it 10 times
d10 = Dice(sides=20)
results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("10 rolls of a 10-sided dice:")
print(results)

#make a 20 side dice and roll it 10 times
d20 = Dice(sides=20)
results = []
for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("10 rolls of a 20-sided dice:")
print(results)
