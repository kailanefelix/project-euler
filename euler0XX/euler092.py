count = 0
goes_to_1, goes_to_89 = {1}, {89}
for number in range(1, 10**7):
    sequence = {number}
    while True:
        digit_sum = sum(int(i)**2 for i in str(number))
        sequence.add(digit_sum)
        if digit_sum in goes_to_1:
            goes_to_1 = goes_to_1 | sequence
            break
        if digit_sum in goes_to_89:
            goes_to_89 = goes_to_89 | sequence
            count = count + 1
            break
        number = digit_sum

print(count)