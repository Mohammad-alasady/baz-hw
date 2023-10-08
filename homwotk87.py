n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

numbers.sort(reverse=True)

for num in numbers:
    print(num)
