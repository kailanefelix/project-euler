import itertools

from numbertools import is_prime

count, total = 0, 0
numbers = itertools.count(11, step=2)


def truncated(n: int):
    s = str(n)
    for i in range(1, len(s)):
        yield int(s[i:])
        yield int(s[:-i])


while count < 11:
    number = next(numbers)

    if is_prime(number) and all(is_prime(n) for n in truncated(number)):
        count = count + 1
        total = total + number

print(total)