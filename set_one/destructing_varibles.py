a, s, d, f, g = [1, 2, 3, 4, 5]
print(a)

z, x, c = {'cat': 3, 'dog': 5, 'fox': 10}
print(x)

example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
    print(counter, letter)

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# ignoring
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic

for _ in range(10):
    print('i')

# collect values
head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
