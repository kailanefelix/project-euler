from itertools import count

from numbertools import is_prime

max_n, n = 1, 1
for i in count(2):
    if not is_prime(i):
        continue

    max_n, n = n, n * i
    if n > 1000000:
        break

print(max_n)