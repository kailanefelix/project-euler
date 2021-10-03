total, number, step = 1, 1, 2

for _ in range(500):
    for _ in range(4):
        number = number + step
        total = total + number
    step = step + 2

print(total)