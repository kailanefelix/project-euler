from fractions import Fraction
from itertools import count

def terms_for_e():
    for k in count(2, 2):
        yield 1
        yield k
        yield 1

def drop(sequence, n):
    for _, value in zip(range(n), sequence):
        pass
    yield from sequence

def take(sequence, n):
    for _, value in zip(range(n), sequence):
        yield value

def continued_fractions(a0, an):
    frac = Fraction(0)
    for ai in reversed(an):
        frac = Fraction(1, ai + frac)
    return a0 + frac

terms = [*take(terms_for_e(), 99)]
e_fraction = continued_fractions(2, terms)
digits = str(e_fraction.numerator)
print(sum(int(n) for n in digits))
