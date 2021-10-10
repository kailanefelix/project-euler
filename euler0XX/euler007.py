from numbertools import is_prime

count = 1
n = 1
while count < 10001:
    n = n + 2
    if is_prime(n):
        count = count + 1

print(n)
