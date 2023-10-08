a = int(input())
b = 0
c = 1

while a > 0:
    k = a % 10
    if k != 0:
        b += k * c
        c *= 10
    a //= 10

print(b)


    