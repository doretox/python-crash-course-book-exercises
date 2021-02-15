# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# •Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

#using the program from exercise 8

cubes = []

for number in range(1,12):
    cubes.append(number**3)

print("The whole list are: " + str(cubes) + "\n")

print("The first three itens in the list are: " + str(cubes[:3]) + "\n")

print("The three itens from the middle of the list are: " + str(cubes[4:7]) + "\n")

print("The last three itens in the list are: " + str(cubes[:-3]))