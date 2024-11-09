def new_sum(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_


print(new_sum(1, 5, 3, 4, 5))
