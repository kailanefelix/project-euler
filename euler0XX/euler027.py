from euler0xx.numbertools import is_prime
from itertools import count

max_sequence = 0
for b in range(-1000, 1001):
    if not is_prime(b):
        continue

    for a in range(-999, 1000):
        sequence = 0
        for n in count(0):
            number = n * n + (a + (b + 1) % 2) * n + b
            if not is_prime(number):
                break

            sequence = sequence + 1

        if sequence > max_sequence:
            max_sequence = sequence
            product = a * b

print(product)