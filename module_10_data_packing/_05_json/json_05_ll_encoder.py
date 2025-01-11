import json


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    @staticmethod
    def class_to_dict(obj):
        return obj.__dict__


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def to_list(self):
        list_data = []
        node = self.head
        while node is not None:
            list_data.append(node.data)
            node = node.next_node
        return list_data

    def print_ll_from_head(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next_node

    def print_ll_from_tail(self):
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev_node


class MyLLDataEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            'head': o.head.data,
            'tail': o.tail.data,
            'num_of_elements': len(o.to_list()),
            'ClassName': o.__class__.__name__,
            'data': o.to_list()
        }


cats_list = LinkedList()
cats_list.insert_at_head("Барсик_1")
cats_list.insert_at_head("Снежок_0")
cats_list.insert_at_tail("Персик_2")

json_cats_list = json.dumps(cats_list, cls=MyLLDataEncoder, ensure_ascii=False, indent=2)
print(json_cats_list)
python_cats_list = json.loads(json_cats_list)
print(python_cats_list)

with open(r'json_files\my_cat_ll_encode.json', 'w', encoding='utf-8') as fh:
    json.dump(cats_list, fh, cls=MyLLDataEncoder, ensure_ascii=False, indent=4)

with open(r'json_files\my_cat_ll_encode.json', 'r', encoding='utf-8') as fh:
    python_cat_from_file = json.load(fh)
print(python_cat_from_file)