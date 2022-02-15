"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
so the user can continue entering numbers even if they make a mistake and 
enter text instead of a number
"""

while(True):
      
    try:
        n1 = int(input("Type a number: "))
        n2 = int(input("Typer another number: "))
        sum = n1+n2

        print("The sum is: ", sum)
    except ValueError:
        print("You can't sum a letter!")
    
    cont = input(("Do you want to sum 2 more numbers? (y/n): "))

    if cont == 'n':
        break
