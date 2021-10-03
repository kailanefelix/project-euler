from math import sqrt

def is_pentagonal(number):
    n = (1 + sqrt(1 + 24 * number)) / 6
    return n.is_integer()

flag, n1 = False, 1

while not flag:
    p1 = n1 * (3 * n1 - 1) // 2

    for n2 in range(n1 - 1, 0, -1):
        p2 = n2 * (3 * n2 - 1) // 2
        if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
             print(p1 - p2)
             flag = True
             break
    n1 = n1 + 1