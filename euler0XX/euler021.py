def divisors(n):
    yield 1

    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        yield sqrt

    for i in range(2, sqrt):
        if n % i == 0:
            yield i
            yield n // i

total = 0
for n in range(3, 10001):
    sum_divs = sum(divisors(n))

    if n == sum_divs:
        continue

    if sum(divisors(sum_divs)) == n:
        total = total + n

print(total)