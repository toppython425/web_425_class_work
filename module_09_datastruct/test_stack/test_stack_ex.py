import unittest

from module_09_datastruct._01_Stack.stack_05 import Node, Stack


class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, node_1)
        self.assertEqual(node_2.next_node.data, 5)


class TestStack(unittest.TestCase):
    stack_test = Stack(2)

    def test_1_init(self):
        self.assertEqual(self.stack_test.top, None)
        self.assertEqual(self.stack_test.stack_size, 2)
        self.assertEqual(self.stack_test.counter, 0)

    def test_2_push(self):
        self.stack_test.push('bottom_data')
        self.stack_test.push('top_data')
        self.assertEqual(self.stack_test.top.data, 'top_data')
        self.assertEqual(self.stack_test.top.next_node.data, 'bottom_data')
        self.assertEqual(self.stack_test.push('overflow_data'), 'Stack overflow!')
        self.assertEqual(self.stack_test.counter, 2)
        self.stack_test.pop()
        self.stack_test.pop()

    def test_3_pop(self):
        self.stack_test.push('test_data')
        self.assertEqual(self.stack_test.pop(), 'test_data')
        self.assertEqual(self.stack_test.top, None)
        self.assertEqual(self.stack_test.counter, 0)

    def test_4_counter_int(self):
        self.stack_test.push(1)
        self.stack_test.push('top_data')
        self.assertEqual(Stack.counter_int(self.stack_test), 1)
        self.stack_test.pop()
        self.stack_test.pop()

    def test_5_stack_empty(self):
        self.assertEqual(self.stack_test.is_stack_empty(), True)
        self.stack_test.push(1)
        self.assertEqual(self.stack_test.is_stack_empty(), False)
