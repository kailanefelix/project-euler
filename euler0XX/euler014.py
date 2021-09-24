max_t, max_n = 1, 1

for n in range(2, 1_000_000):
    terms = 1

    i = n
    while i != 1:
        i = i / 2 if i % 2 == 0 else 3 * i + 1
        terms = terms + 1

    if terms > max_t:
        max_t, max_n = terms, n

print(max_n)
