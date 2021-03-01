class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is representation of the object in custom string type (in this case)
    # __str__ will run and __repr__ will not run in this case
    def __str__(self):
        return 'jello'

    # __repr__ is used in other cases, like debugger
    def __repr__(self):
        return f'<Person({self.name}, {self.age}>'

    def tell_name(self):
        print(self.name)


person = Person('Mike', 23)
person.tell_name()
print(person)
print(person.__repr__())
