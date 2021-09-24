from math import factorial

width, height = 20, 20
print(factorial(width + height) // (factorial(width) * factorial(height)))