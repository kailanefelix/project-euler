from datetime import date

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if date(year, month, 1).weekday() == 6:
            sundays = sundays + 1
print(sundays)

print(sum(
    date(year, month, 1).weekday() == 6
    for year in range(1901, 2001)
    for month in range(1, 13)
))

