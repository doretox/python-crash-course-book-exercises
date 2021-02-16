# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •Tests for equality and inequality with strings
# •Tests using the lower() function
# •Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# •Tests using the and keyword and the or keyword
# •Test whether an item is in a list
# •Test whether an item is not in a list

car = 'Tesla'
print("car = 'tesla'? " + str(car == 'tesla') + "\n")

print("car.lower() == 'Tesla'? " + str(car.lower() == 'tesla') + "\n") 

print("Is 1 > 5? " + str(1 > 5) + "\n")

print("Is 3 < 8? " + str(3 < 8) + "\n")

print("Is 4 == 4? " + str(4 == 4) + "\n")

print("Is 4 >= 7? " + str(4 >= 7) + "\n")

print("Is 4 <= 7? " + str(4 <= 7) + "\n")

print("Is 4 and 3 <= 7? " + str(4 and 3 <= 7) + "\n")

print("Is 9 and 6 >= 12? " + str(9 and 6 >= 12) + "\n")

list = [1, 2, 3, 4, 5, 6, 7]

print(list)
print("Is 4 in the list? " + str(4 in list) + "\n")

print("Is 6 not in the list? " + str(6 not in list) + "\n")