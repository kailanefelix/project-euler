from functools import lru_cache
from math import ceil


def divisors(n: int):
    yield 1

    sqrt = n ** 0.5
    if sqrt.is_integer():
        yield int(sqrt)

    for i in range(2, ceil(sqrt)):
        if n % i == 0:
            yield i
            yield n // i

@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Fermat
    if pow(2, n - 1, n) != 1:
        return False

    for i in range(5, int(n**(1 / 2)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True
