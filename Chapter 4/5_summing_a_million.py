# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers = []

for number in range(1, 1000001):
    numbers.append(number)

#max
print("the maximum value is: " + str(max(numbers)))

#min
print("The minimum value is: " + str(min(numbers)))

#sum
print("The sum of all values is: " + str(sum(numbers)))
