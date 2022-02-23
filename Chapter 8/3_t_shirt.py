"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(size, text):
    """Display a size and a message in a T-shirt."""
    print("The T-shirt size is: " + size.title())
    print("And it says : " + text.title())

make_shirt('l', 'life is beautiful')

make_shirt(size='s',text='i love coffe')