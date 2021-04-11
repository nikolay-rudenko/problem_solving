import pprint

# describe how to produce object
class ObjectCreator(object):
    pass

my_object = ObjectCreator()

# class itself is an object
# print(ObjectCreator)

def echo(o):
    print(o)

# echo(ObjectCreator) # assign class as a parametr
ObjectCreator.new_attribute = 'foo' # you can add attributes to a class
print(hasattr(ObjectCreator, 'new_attribute')) # you can add attributes to a class
# pprint.pprint(globals())

ObjectCreatorMirror = ObjectCreator # you can assign a class to a variable

print(ObjectCreatorMirror.new_attribute)

# Creating classes dynamically

def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
MyClass = choose_class('foo')
print(MyClass)
print(MyClass()) # you can create an object from this class

'''
Well, type has a completely different ability, 
it can also create classes on the fly. 
type can take the description of a class as parameters, 
and return a class.
'''
print(type(ObjectCreator))
print(type(ObjectCreator()))

# for example
MyShinyClass = type('MyShinyClass', (), {})
print(MyShinyClass)
print(MyShinyClass())

# type accepts a dictionary to define
# the attributes of the class.

class Foo(object):
    bar = True

Fooo = type('Foo', (), {'bar': True, 'cat': 'Angry'})
print(Fooo)
print(Fooo())
print(Fooo.cat)

f = Foo()
print(f)

# inherit
class FoooChield(Fooo):
    pass

f = FoooChield()
print(f.cat)

FoooChild = type('FooChild', (Fooo,), {})
print(FoooChild)
print(FoooChild.bar)

# include method
def echo_bar(self):
    print(self.bar)

FoooChieldish = type('FooChild', (Fooo,), {'echo_bar': echo_bar})
print(hasattr(Fooo, 'echo_bar'))
print(hasattr(FoooChieldish, 'echo_bar'))

# add more methods
def echo_bar_more(self):
    print('yet another method')

FoooChieldish.echo_bar_more = echo_bar_more
print(hasattr(FoooChieldish, 'echo_bar_more'))

'''
Metaclasses are the 'stuff' that creates classes.
You define classes in order to create objects, right?
But we learned that Python classes are objects.
Well, metaclasses are what create these objects. 
They are the classes' classes, you can picture them this way:
MyClass = MetaClass()
my_object = MyClass()
'''
MyClass = type('MyClass', (), {})

'''
It's because the function type is in fact a metaclass. 
type is the metaclass Python uses 
to create all classes behind the scenes.

'''