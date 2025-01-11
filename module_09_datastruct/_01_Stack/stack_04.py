class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data

#
# if __name__ == '__main__':
#
#     # node_1 = Node('5_RUB', None)
#     # node_2 = Node('7_RUB', node_1)
#     # node_3 = Node('10_RUB', node_2)
#     #
#     # print(node_1.data)
#     # print(node_2.data)
#     # print(node_2.next_node.data)
#     # print(node_3.next_node.next_node.data)
#
#     my_stack = Stack()
#     my_stack.push('data_3')
#     my_stack.push('data_2')
#     my_stack.push('data_1')
#
#     # print(my_stack.top.data)
#     # print(my_stack.top.next_node.data)
#     # print(my_stack.top.next_node.next_node.data)
#
#     # print(my_stack.pop())
#     # print(my_stack.pop())
#     # print(my_stack.pop())
#     stack_len = round(len(my_stack.top.data))
#     print(stack_len)
#
#     try:
#         for i in range(100):
#             print(my_stack.pop())
#     except AttributeError:
#         print('Stack is Empty')
#     finally:
#         print("Data extracted")


