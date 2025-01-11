from module_10_data_packing._02_data_packing_pickle_difficult._pickle_difficult import LinkedList
from module_10_data_packing._03_data_packing_pikle_classes._03_pickler_classes import MyPickler, MyUnpickler

if __name__ == '__main__':
    my_pickler_5 = MyPickler(protocol=5)
    my_pickler_4 = MyPickler()
    box_list = LinkedList()
    box_list.insert_at_head('Барсик_1')
    box_list.insert_at_head('Снежок_0')
    box_list.insert_at_tail('Персик_2')

    box_list = my_pickler_5.pickle_data(box_list)
    box_list = MyUnpickler.unpickle_data(box_list)
    box_list.print_ll_from_head()
    print()
    my_pickler_4.pickle_file('ll_pickle.cats', box_list)
    box_list = MyUnpickler.unpickle_file('ll_pickle.cats')
    box_list.print_ll_from_tail()
