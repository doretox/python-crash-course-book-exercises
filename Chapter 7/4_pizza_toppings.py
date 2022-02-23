"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you'll add that topping to their pizza.
"""

message = "Please enter a topping for your pizza: "
message += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(message)
    
    if topping == 'quit':
        break
    else:
        print("You addded: " + topping + " to your pizza.")
