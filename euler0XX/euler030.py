total = 0

for number in range(10, 10 ** 6):
    digitSum = sum(int(digit) ** 5 for digit in str(number))
    if digitSum == number:

         total = total + number

print(total)
