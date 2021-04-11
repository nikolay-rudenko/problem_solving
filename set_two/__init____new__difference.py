x = (1, 2) # this is not mutable type, this is why output (1, 2)
x.__init__([3, 4])
print(x)

y = [1, 2] # because this is mutable type, this is why output [3, 4]
y.__init__([3, 4])
print(y)

x.__new__([3, 4])
# and here, is the type error,
# tuple.__new__(X): X is not a type object (list)
# this is because __new__ take type like a first argument
print(x)
