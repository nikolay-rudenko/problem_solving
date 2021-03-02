class ClassTest:
    def instance_method(self):
        print(f'instance_method of {self} called')

    @classmethod
    def class_method(cls):
        print(f'class_method of {cls} called')

    @staticmethod
    def static_method():
        print(f'static_method called')


test = ClassTest()
test.instance_method()

ClassTest.class_method()
ClassTest.static_method()

