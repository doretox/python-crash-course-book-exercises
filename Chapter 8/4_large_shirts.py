# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a 
# different message.

def make_shirt(size='l', text='I love python!'):
    """Display a size and a message in a T-shirt."""
    print("The T-shirt size is: " + size.title())
    print("And it says : " + text.title())

make_shirt()
make_shirt(size='M')
make_shirt(size='xl',text='I love c++')