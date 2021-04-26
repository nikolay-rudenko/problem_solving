height = [154, 145, 152, 161, 176, 189, 145, 170, 145]

def average(array):
    unique = set(array)
    num_sum = sum(unique)
    num_len = len(unique)
    num_float = format(num_sum/num_len, '.3f')

    return num_float


print(average(height))
