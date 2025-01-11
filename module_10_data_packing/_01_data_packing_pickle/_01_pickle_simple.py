import pickle

my_data = {
    'nums': [1, 2, 3, 4, 5 + 5],
    'strings': ['character_string', b'byte_string'],
    'other': [None, True, False]
}

# для обычной работы
my_data_s = pickle.dumps(my_data, pickle.HIGHEST_PROTOCOL)
print(my_data_s)
my_data_ds = pickle.loads(my_data_s)
print(my_data_ds)

with open('data_pickle.pkl', 'wb') as fp:
    pickle.dump(my_data_ds, fp, protocol=5)

try:
    with open('data_pickle.pkl', 'rb') as fp:
        my_data_ff = pickle.load(fp)
except FileNotFoundError:
    print('Файл не найден!')

print(my_data_ff)

