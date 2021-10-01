with open('euler067_triangle.txt') as fp:
    triangle = [[int(n) for n in line.split(' ')] for line in fp]

def maximize(triangle):
    triangle = triangle[:]
    for i in range(len(triangle) - 2, -1, -1):
        for j, value in enumerate(triangle[i]):
            triangle[i][j] = value + max(triangle[i + 1][j:j + 2])
    return triangle[0][0]

print(maximize(triangle))
