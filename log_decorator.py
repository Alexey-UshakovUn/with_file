from time import time, asctime
from datetime import datetime
import os


def recursive(number):
    while True:
        if number in (1, 2):
            return 1
        else:
            return recursive(number - 1) + (recursive(number - 2))


def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        work_time = time() - start_time
        log = '{}: func - {}, work time {}'.format(datetime.now(), func.__name__, work_time)
        with open('log', 'at+') as file:
            file.write(log + '\n')
        return work_time

    return wrapper


if __name__ == '__main__':
    get_time = log_decorator(recursive)
    print(get_time(20))
