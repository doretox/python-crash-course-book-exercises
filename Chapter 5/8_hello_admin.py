# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
# ging in again.

usernames = ['pedro', 'john', 'charlie', 'admin', 'mark']

for username in usernames:
    if username == 'admin':
        print("Hello ADMIN, would you like to see a status report?\n")
    else:
        print("Hello " + str(username.title()) + " thank you for logging"
        " in again.\n")