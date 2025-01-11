import pickle


def unpickle_file(pickled_filename):
    try:
        with open(pickled_filename, 'rb') as fp:
            unpickle_data = pickle.load(fp)
    except FileNotFoundError:
        return 'Файл не найден!'
    return unpickle_data


unpickle_file('bomb.bm')
