n = int(input())
is_increasing = True
prev_num = float()
for i in range(n):
    num = int(input())
    if num < prev_num:
        is_increasing = False
        break
    prev_num = num
if is_increasing:
    print("YES")
else:
    print("NO")
