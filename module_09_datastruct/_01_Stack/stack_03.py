from stack_02 import Stack


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val

class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        if self.__sum > 10:
            print("Stack Overflow")
            self.__sum -= val
            return
        super().push(val)

    def pop(self):
        val = super().pop()
        self.__sum -= val
        return val


if __name__ == '__main__':
    stack_object = AddingStack()
    for i in range(6):
        stack_object.push(i)
    print(f'Сумма внутри стека {stack_object.get_sum()}')
    for i in range(5):
        print(f'Значение {stack_object.pop()}. Сумма внутри стека {stack_object.get_sum()}')
