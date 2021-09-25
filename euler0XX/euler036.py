total = 0
for number in range(1_000_000):
    as_str = str(number)
    if as_str == as_str[::-1]:
        as_bin = f'{number:b}'
        if as_bin == as_bin[::-1]:
            total = total + number

print(total)