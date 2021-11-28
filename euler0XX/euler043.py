from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

total = 0
for n in permutations('0123456789'):
    for i, prime in enumerate(primes):
        number = ''.join(n[i+1:i+4])
        if int(number) % prime != 0:
            break

    else:
        total = total + int(''.join(n))

print(total)