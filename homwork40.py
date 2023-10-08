num1 = input()
num2 = input()

if len(num1) == 3 and len(num2) == 3:
    result = ""
    carry = 0

    for i in range(2, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        total = bit1 + bit2 + carry
        result = str(total % 2) + result
        carry = total // 2

    if carry:
        result = "1" + result

    print(result)

