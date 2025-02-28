import sys
import random


a = []
b = []
for i in sys.stdin:
    a.append(i)
    b.append(i)
while True:
    random.shuffle(b)
    if not any(a[i] == b[i] for i in range(len(a))):
        break
for i in range(len(a)):
    print(f'{a[i]} - {b[i]}')