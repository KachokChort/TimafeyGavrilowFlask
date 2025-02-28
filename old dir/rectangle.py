a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

ax1, ay1, ax2, ay2 = a[0], a[1], a[0] + a[2], a[1] + a[3]
bx1, by1, bx2, by2 = b[0], b[1], b[0] + b[2], b[1] + b[3]

if ay1 > bx2 or ay2 < by1 or bx2 < ax1 or ax2 < bx1:
    print('No')
else:
    print('Yes')