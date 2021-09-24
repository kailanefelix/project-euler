tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

units = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}


def spell(n: int) -> str:
    if n == 1000:
        return "one thousand"
    if n >= 100:
        s = f'{spell(n // 100)} hundred'
        return s if n % 100 == 0 else f'{s} and {spell(n % 100)}'
    if n >= 20:
        s = tens[n // 10]
        return s if n % 10 == 0 else f'{s} {units[n % 10]}'
    return units[n]


def letters(s):
    return len(''.join(s.split(' ')))


print(sum(letters(spell(n)) for n in range(1, 1001)))