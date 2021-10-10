from numbertools import divisors

numbers = {*range(28124)}

abundant = {n for n in range(12, 28112) if sum(divisors(n)) > n}
abundant_sums = {a + b for a in abundant for b in abundant}

print(sum(numbers - abundant_sums))