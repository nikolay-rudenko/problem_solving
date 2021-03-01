def add(x, y):
    return x + y


nums = [1, 3] # list
assert add(*nums) == 4

nums = {2, 3} # set
assert add(*nums) == 5

# unpacking the dictionary
nums = {'x': 3, 'y': 3}
assert add(**nums) == 6
