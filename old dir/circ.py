a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

s = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
print(s)
if s <= a[2] + b[2]:
    print('YES')
else:
    print('NO')
