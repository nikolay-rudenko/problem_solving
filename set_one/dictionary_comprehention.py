# creating the list with data
users = [
    (0, 'Sam', 'pasd8gh'),
    (1, 'Bodhi', 'Budja88'),
    (2, 'ODin', 'toby001'),
    (3, 'Mask', 'ilovenasa99'),
]

# creating data on dictionary with a purpose use less code and not use for loops
user_mapping = {user[1]: user for user in users}

# user entering credentials
user_name_input = input('enter your name')
user_password_input = input('enter your password')

# destructuring the dictionary to the variables, to verify user data
_, name, password = user_mapping[user_name_input]

if password == user_password_input:
    print('logged')
else:
    print('wrong password or username')
