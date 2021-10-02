from itertools import count

for h in count(144):
    y = 2 * h * h - h
    p = (1 + (1 + 24 * y) ** 0.5) / 6
    if p.is_integer():
        print(y)
        break