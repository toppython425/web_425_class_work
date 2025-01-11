queue = []


def enqueue(data):
    queue.append(data)


def dequeue():
    # if len(queue) == 0:
    if not queue:
        return 'Очередь пуста'
    return queue.pop(0)


def peek_first():
    if not queue:
        return 'Очередь пуста'
    return queue[0]


def peek_last():
    if not queue:
        return 'Очередь пуста'
    return queue[-1]


def size():
    return len(queue)


enqueue('data_1')
enqueue('data_2')
enqueue('data_3')
enqueue('data_4')
print(peek_first())
print(peek_last())
print(size())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
