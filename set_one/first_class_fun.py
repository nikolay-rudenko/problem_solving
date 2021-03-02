from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}.')


friends = [
    {'name': 'Nick', 'age': 33},
    {'name': 'Augustin', 'age': 12},
    {'name': 'Ragnar', 'age': 34}
]


def get_friends_name(friend):
    return friend['name']


# print(search(friends, 'Nickx', get_friends_name))
# print(search(friends, 'Nick', lambda friend: friend['name']))
print(search(friends, 'Nick', itemgetter('name')))