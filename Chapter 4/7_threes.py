# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

from abc import abstractproperty


multiples = []

for number in range(3, 31, 3):
    multiples.append(number)

print(multiples)