import sys

p = []
sum = 0
k = 0
for line in sys.stdin:
    h = int(line.strip())
    p.append(h)
if len(p) == 0:
    print('-1')
else:
    for i in p:
        sum += i
        k += 1
    print(sum / k)