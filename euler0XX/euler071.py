max_fraction, numerator = 0, 0
for d in range(2, 1_000_001):
    for n in range(ceil(d * max_fraction), int(3 * d / 7)):
        if gcd(n, d) == 1:
            max_fraction = n / d
            numerator = n
print(numerator)
