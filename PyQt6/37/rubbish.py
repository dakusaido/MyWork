import random

a = list(range(100000))
b = a
random.shuffle(a)


def selection(data):
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data

import time

f_time = time.time()
a.sort()
print(time.time() - f_time)
f_time = time.time()
selection(b)
print(time.time() - f_time)