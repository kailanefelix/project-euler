from primality import is_prime

limit = 1_000_000

primes = [2, *(i for i in range(3, limit, 2) if is_prime(i))]

max_sum, longest = 0, 1
for i in range(1, len(primes)):
    for j in range(longest + 2, i, 2):
        new_sum = sum(primes[i - j:i])
        if new_sum >= limit:
            break

        if is_prime(new_sum):
            longest = j
            max_sum = new_sum

print(max_sum, longest)