#Sum of Numbers Divisible by 3 from 1 to 100

total = 0

for i in range(1, 101):
    if i % 3 == 0:
        total += i

print(total)