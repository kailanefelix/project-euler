from fractions import Fraction

total = Fraction(1)
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            num = a * 10 + b
            den = b * 10 + c
            if num >= den:
                continue

            f = Fraction(num, den)
            if f == Fraction(a, c):
                total = total * f

print(total.denominator)