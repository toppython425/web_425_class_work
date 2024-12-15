class ExampleClass:

    def __init__(self, first=1, second=2):
        self.first = first
        self.second = second
        # self.third = 5 # только для объекта example_object_3

    def set_second(self, second):
        self.second = second


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
