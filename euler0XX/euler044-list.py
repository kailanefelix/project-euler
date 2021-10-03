from itertools import count
from math import sqrt

def is_pentagonal(number):
    n = (1 + sqrt(1 + 24 * number)) / 6
    return n.is_integer()

prev = []
for i in count(1):
    pk = i * (3 * i - 1) // 2

    for pj in prev:
        if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
            print(pk - pj)
            break

    else:
        prev.append(pk)
        continue

    break
