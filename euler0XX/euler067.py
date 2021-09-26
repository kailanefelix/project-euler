with open("euler067_triangle.txt", "r") as fp:

    triangle = []
    for line in fp: 
        numbers = line.split()

        l = []
        for i in numbers:
            integer = int(i)
            l.append(integer)

        triangle.append(l)

for row in range(len(triangle) - 2, -1, -1):
    line = triangle[row]
    for col in range(len(line)):
        adjacent = triangle[row + 1][col:col + 2]
        triangle[row][col] = triangle[row][col] + max(adjacent)

print(triangle[0][0])