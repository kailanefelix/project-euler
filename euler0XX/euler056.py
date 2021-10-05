max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        p = a ** b
        p_sum = sum(int(i) for i in str(p))
        if p_sum > max_sum:
            max_sum = p_sum
print(max_sum)
