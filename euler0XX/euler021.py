from numbertools import divisors

total = 0
for n in range(3, 10001):
    sum_divs = sum(divisors(n))

    if n == sum_divs:
        continue

    if sum(divisors(sum_divs)) == n:
        total = total + n

print(total)