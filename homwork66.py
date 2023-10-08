def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num
sum=0
for i in range (100):
    a=int(input())
    if a%2!=0 and is_fibonacci:
        sum+=1
print(sum)