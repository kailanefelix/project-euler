from itertools import count

for number in count(1):
    digits = sorted(str(number))

    for n in range(2, 7):
        product = sorted(str(number * n))
        if digits != product:
            break

    else:
        print(number)
        break