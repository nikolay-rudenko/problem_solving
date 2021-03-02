def data(**kwargs):
    # print(kwargs)
    pass


my_dict = {'name': 'Bob', 'age': 34}
data(**my_dict)


def accept_infinite_data(*args, **kwargs):
    print(args)
    print(kwargs)


accept_infinite_data(2, 4, 5, 6, 6, sam='name', cat='dog')
