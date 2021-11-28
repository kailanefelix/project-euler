from numbertools import is_prime

total = 0
for i in range(2000000):
    if is_prime(i):
        total = total + i