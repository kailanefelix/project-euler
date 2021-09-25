from math import factorial

total = 0
for number in range(10, 2540160):
    if number == sum(factorial(int(digit)) for digit in str(number)):
        total = total + number

print(total)