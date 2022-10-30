from time import time


def time_work(func):
    def wrapper(*args, **kwargs):
        first = time()
        value = func(*args, **kwargs)
        return value, time() - first

    return wrapper


@time_work
def rect_area(a, b):
    return float(a) * float(b)


print(rect_area(1, 2))
print(rect_area(2.4, 4))

