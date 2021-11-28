import time

from numbertools import is_prime


def rotations(s: str):
    for i in range(1, len(s)):
       yield s[i:] + s[:i]

start = time.process_time()

count = 4
for number in range(11, 1000000, 2):
    if is_prime(number) and all(is_prime(int(rotation)) for rotation in rotations(str(number))):
        count = count + 1

elapsed_time = time.process_time() - start

print(count, f'{elapsed_time * 1000:.3f} ms')