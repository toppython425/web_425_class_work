from threading import Thread, Lock
from time import sleep


class Counter:

    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increase(self, by):
        self.lock.acquire()
        current_value = self.value
        current_value += by
        sleep(0.5)

        self.value = current_value
        print(f'Значение value: {self.value}')

        self.lock.release()


counter = Counter()

thread1 = Thread(target=counter.increase, args=(10, ))
thread2 = Thread(target=counter.increase, args=(20, ))
thread3 = Thread(target=counter.increase, args=(30, ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f'Значение value в итоге: {counter.value}')
