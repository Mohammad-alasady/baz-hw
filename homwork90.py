n = int(input())
n = n+1
factorials = [1]

for i in range(1, n):
    factorial = factorials[-1] * i
    factorials.append(factorial)

for i in range(1, n):
    print(factorials[i])

