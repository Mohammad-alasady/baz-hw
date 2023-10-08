def zoj(sum):
    for i in range(5):
        a = int(input())
        if a % 2 == 0:
            sum = sum + 1
    return sum

sum = 0
result = zoj(sum)
print(result)
 