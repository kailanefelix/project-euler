from fractions import Fraction


def continued_fractions(a0, an):
    frac = Fraction(0)
    for ai in reversed(an):
        frac = Fraction(1, ai + frac)
        yield a0 + frac


count = 0
for f in continued_fractions(1, [2] * 1000):
    if len(str(f.numerator)) > len(str(f.denominator)):
        count = count + 1

print(count)