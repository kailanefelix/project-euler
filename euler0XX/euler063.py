import itertools

count = 0
for base in range(1, 10):
    for exp in itertools.count(1):
        digits = len(str(base ** exp))

        if digits < exp:
            break

        if digits == exp:
            count = count + 1

print(count)