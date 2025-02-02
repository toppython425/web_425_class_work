import threading


def print_numbers():
    for i in range(10):
        print(i)


thread1 = threading.Thread(target=print_numbers)
thread1.start()
