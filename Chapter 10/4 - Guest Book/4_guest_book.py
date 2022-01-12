#10-4. Guest Book: Write a while loop that prompts users for their name. When 
#they enter their name, print a greeting to the screen and add a line #recording their visit in a file called guest_book.txt. Make sure each entry #appears on a new line in the file.

filename = 'guest_book.txt'

print("Enter 'exit' to finish.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'exit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")