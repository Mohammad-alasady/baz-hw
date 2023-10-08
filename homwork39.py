a = int(input())
sum = 0

if a % 10 == 1:
    sum = sum * 10 + 1

if (a // 10) % 10 == 1:
    sum = sum * 10 + 1

if (a // 100) % 10 == 1:
    sum = sum * 10 + 1

if (a // 1000) % 10 == 1:
    sum = sum * 10 + 1

print(sum)
