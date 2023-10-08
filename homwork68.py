a = int(input())
sum = 0
while a > 0:
    sefr = a % 10
    if sefr == 0:
        sum += 1
    a //= 10
print(sum)    