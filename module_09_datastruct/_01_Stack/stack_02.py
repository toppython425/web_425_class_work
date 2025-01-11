class Stack:
    all_stack_list = []

    def __init__(self):
        self.__stack_list = []
        Stack.all_stack_list.append(self)

    def push(self, val):
        if val == "Stack is empty":
            return
        self.__stack_list.append(val)

    def pop(self):
        try:
            val = self.__stack_list.pop()
        except IndexError:
            return "Stack is empty"
        return val

    def get_stack(self):
        return self.__stack_list

    def remove_from_stack_list(self):
        Stack.all_stack_list.remove(self)


if __name__ == '__main__':
    stack_object_1 = Stack()
    stack_object_2 = Stack()
    stack_object_1.push(3)
    stack_object_1.push(2)
    stack_object_1.push(1)
    stack_object_2.push(stack_object_1.pop())
    stack_object_2.push(stack_object_1.pop())
    stack_object_2.push(stack_object_1.pop())
    stack_object_2.push(stack_object_1.pop())
    stack_object_2.push(stack_object_1.pop())
    print(stack_object_2.get_stack())
    print(stack_object_2.pop())
    print(stack_object_2.pop())
    print(stack_object_2.pop())
    print(stack_object_2.pop())

    print(Stack.all_stack_list)
    stack_object_1.remove_from_stack_list()
    print(Stack.all_stack_list)
