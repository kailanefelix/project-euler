factors = [0] * 1000000

for i in range(2, len(factors)):
    if factors[i] == 0:
        for j in range(i + i, len(factors), i):
            factors[j] = factors[j] + 1

    if factors[i:i + 4] == [4, 4, 4, 4]:
        print(i)
        break