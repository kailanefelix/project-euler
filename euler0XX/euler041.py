from itertools import permutations

from numbertools import is_prime

digits = '987654321'

for n in range(9):
    for permutation in permutations(digits[n:]):
        number = int(''.join(permutation))     
        if is_prime(number):
            print(number)
            break

    else:
        continue
    
    break