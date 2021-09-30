max_count, max_p = 0, 0

for p in range(12, 1000, 2):
    count = 0
    
    for a in range(1, p // 3):
        for b in range(a, 2 * (p // 3) - a):
            c = p - a - b
            if c * c == a * a + b * b:
                count = count + 1

    if count > max_count:
        max_count, max_p = count, p

print(max_p)