from euler0xx.numbertools import phi

total = 0
for n in range(2, 1_000_001):
    total = total + phi(n)
print(total)

# parallel
from multiprocessing import Pool

with Pool() as p:
    total = sum(p.imap_unordered(phi, range(2, 1_000_001)))
print(total)
