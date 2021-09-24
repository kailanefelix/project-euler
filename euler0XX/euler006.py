sum_of_squares = 0
for number in range(101):
    sum_of_squares = sum_of_squares + number * number

square_of_sum = 0
for number in range(101):
    square_of_sum = square_of_sum + number
square_of_sum = square_of_sum * square_of_sum

print(square_of_sum - sum_of_squares)
