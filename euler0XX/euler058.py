from itertools import count
from numbers import is_prime

primes, total, number, step = 0, 0, 1, 2

for i in count():
    for _ in range(4):
        number = number + step

        if is_prime(number):
            primes = primes + 1
        total = total + 1

    step = step + 2

    if primes / total < 0.1:
        print(2 * i + 1)
        break