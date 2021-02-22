# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the 
# poll.

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
places = {}

while True:
    # Ask the user their name.
    name = input(name_prompt)

    # Ask the user where they'd go.
    place = input(place_prompt)

    # Store the response.
    places[name] = place

    # Ask if the user want to continue.
    repeat = input(continue_prompt)
    if repeat == 'no':
        break

# Show results.
print("\n")
for name, place in places.items():
    print(name.title() + " would like to visit " + place.title() + ".")
