number, i = 1, 2

while True:
    sqrt = int(number**0.5)

    if sum(number % j == 0 for j in range(1, sqrt)) > 250:
        break

    number, i = number + i, i + 1

print(number)
