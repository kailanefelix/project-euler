a, b = 1, 2
total = 0
while a < 4_000_000:
    a, b = b, a + b
    if a % 2 == 0:
        total = total + a
       
print(total)