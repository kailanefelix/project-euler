from itertools import combinations, permutations
from numbertools import is_prime

answers = set()
for n in range(1000, 10000):
    perms = {int(''.join(p)) for p in permutations(str(n))}

    # remove permutations with less than 4 digits (leading 0) and that are not prime
    perms = {p for p in perms if p >= 1000 and is_prime(p)}

    if len(perms) < 3:
        continue

    for a, b, c in combinations(perms, r=3):
        if a - b == b - c:
            answers.add((a, b, c))

for a, b, c in answers:
    print(f'{a}{b}{c}')