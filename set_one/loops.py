# input: 5
# output: 0, 1, 4, 9, 16

def square(n):
    num = []
    for i in range(n):
        num.append(i ** 2)
    return num


print(*square(5))
