from string import ascii_uppercase

with open("euler022_names.txt", "r") as fp:
    names = sorted(name[1:-1] for name in fp.read().split(","))

total = 0

for i, name in enumerate(names, start=1):
    score = i * sum(ascii_uppercase.index(c) + 1 for c in name)
    total = total + score

print(total)

print(sum(
    i * sum(ascii_uppercase.index(c) + 1 for c in name)
    for i, name in enumerate(names, start=1)
))