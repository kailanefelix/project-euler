from itertools import permutations

perms = permutations('0123456789')
for i in range(999999):
    next(perms)
print(''.join(next(perms)))
