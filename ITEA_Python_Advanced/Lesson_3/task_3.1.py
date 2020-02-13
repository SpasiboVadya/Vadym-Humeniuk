import time
import random


def decorator(num_repeat):
    def timeit(func):
        def wrapper(*args):
            start = time.time()
            result = []
            print('Function name is:', func.__name__)
            print(time.time())
            for i in range(num_repeat):
                result.append(func(*args))
            return result
        return wrapper
    return timeit


@decorator(3)
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
        return l


@decorator(4)
def two(range_start, range_end):
    return random.randint(range_start, range_end)


first = one(5)
second = two(10, 20)
