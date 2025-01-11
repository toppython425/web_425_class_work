import copy


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, stack_size=5, top=None):
        self.top = top
        self.stack_size = stack_size
        self.counter = 0

    def push(self, data):
        if self.counter < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
            self.counter += 1
        else:
            print("Stack overflow!")
            return "Stack overflow!"

    def pop(self):
        remove_last = self.top
        self.top = self.top.next_node
        self.counter -= 1
        return remove_last.data

    @staticmethod
    def counter_int(stack):
        temp_stack = copy.deepcopy(stack)
        counter_int = 0
        while not temp_stack.is_stack_empty():
            if isinstance(temp_stack.top.data, int):
                counter_int += 1
            temp_stack.pop()
        return counter_int

    def is_stack_empty(self):
        if self.top is None:
            return True
        return False


# my_stack = Stack(4)
# my_stack.push(1)
# my_stack.push('str')
# my_stack.push(3)
# my_stack.push(0.5)
#
# print(Stack.counter_int(my_stack))
