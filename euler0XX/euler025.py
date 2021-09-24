a, b, i = 1, 1, 1
while a < 10 ** 999:
    a, b, i = b, a + b, i + 1
print(i)