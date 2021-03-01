# lambda PARAMETERS or INPUT: RETURN or OUTPUT

add = lambda x, y: x + y
assert add(5, 5) == 10


def double(x):
    return x * 2


my_list = [1, 2, 3]
doubled = [double(x) for x in my_list]
assert doubled == [2, 4, 6]

doubled = list(map(double, my_list))
assert doubled == [2, 4, 6]

doubled = list(map(lambda x: x * 2, my_list))
assert doubled == [2, 4, 6]
