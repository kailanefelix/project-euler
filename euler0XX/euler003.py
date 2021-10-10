from numbertools import is_prime

n = 600851475143
for i in range(3, n // 2 + 1, 2):
    if n % i == 0 and is_prime(n // i):
        print(n // i)
        break
