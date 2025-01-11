class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_beginning(data)
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def remove_from_beginning(self):
        removed_node = self.head
        self.head = self.head.next_node
        print(f'Удалили: {removed_node.data}.\nТеперь начало {self.head.data}')
        return removed_node.data

    def remove_node_position(self, rm_position):
        if rm_position == 1:
            self.remove_from_beginning()
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return f'Ничего не удалили\nНачало: {self.head.data}'
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удалили: {removed_node.data}.\nНачало {self.head.data}"

    def remove_node_data(self, rm_data):
        if rm_data == self.head.data:
            removed_node = self.head
            self.head = self.head.next_node
            return removed_node.data
        current_node = self.head
        while current_node is not None and current_node.next_node is not None:
            print(current_node.data, current_node.next_node.data)
            if current_node.next_node.data == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                return removed_node.data
            current_node = current_node.next_node
        return f'Ничего не удалили\nНачало: {self.head.data}'

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Информация выведена"

    def contains(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                return True
            current_node = current_node.next_node
        return False

    def get(self, node_position):
        if node_position > self.len_ll():
            return f'В списке нет такого количества элементов, длина списка = {self.len_ll()}'
        current_node_position = 1
        current_node = self.head
        while current_node_position <= node_position:
            if current_node_position == node_position:
                return current_node.data
            current_node_position += 1
            current_node = current_node.next_node

    def len_ll(self):
        items_count = 0
        current_node = self.head
        while current_node:
            items_count += 1
            current_node = current_node.next_node
        return items_count


my_cats_list = LinkedList()
my_cats_list.insert_at_end("Персик_2")
my_cats_list.insert_at_end("Барсик_4")
my_cats_list.insert_at_beginning("Феликс_1")
my_cats_list.insert_at_position("Франц_3", 3)
my_cats_list.insert_at_end("Мурзик_5")

my_cats_list.print_ll()
print()
print(my_cats_list.contains("Барсик_4"))
print(my_cats_list.get(3))
print(my_cats_list.len_ll())
print(my_cats_list.remove_node_position(2))
print(my_cats_list.remove_node_data("Барсик_4"))
print()
my_cats_list.print_ll()
