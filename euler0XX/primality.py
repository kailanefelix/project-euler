def is_prime(n: int) -> bool:

    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False
        
    if pow(2, n - 1, n) != 1:
        return False

    for i in range(5, int(n**(1 / 2)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True