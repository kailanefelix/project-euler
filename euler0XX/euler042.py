from string import ascii_uppercase

triangle_numbers = [n * (n + 1) // 2 for n in range(40)]

with open("euler042_words.txt", "r") as fp:
    words = sorted(word[1:-1] for word in fp.read().split(","))

count = 0
for word in words:
    score = sum(ascii_uppercase.index(letter) + 1 for letter in word)
    if score in triangle_numbers:
        count = count + 1

print(count)