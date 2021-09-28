d = ''.join(str(i) for i in range(1, 10 ** 6))

total = 1
for i in range(7):
    total = total * int(d[10 ** i - 1])
print(total)