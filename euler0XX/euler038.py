from itertools import count

max_concat = ''
for number in range(1, 100000):
    concat = ''
    for n in count(1):
        product = str(number * n)

        if '0' in product:
            break

        concat = concat + product
        if len(concat) >= 9:
            break

    if len(concat) == 9 and len({*concat}) == 9 and concat > max_concat:
        max_concat = concat

print(max_concat)