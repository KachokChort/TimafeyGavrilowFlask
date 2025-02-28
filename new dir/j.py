def f1(a):
    a.lower()
    return a.title()


def f2(a):
    s = ''
    for _ in range(len(a)):
        if _ % 2 == 0:
            s += a[_]
    return s


def f3(a):
    return len(a)


def f4(a):
    s = ''
    s1 = a
    if len(a) % 2 != 0:
        s1 = ''
        for i in a:
            if i not in s:
                s += i
                s1 += i
        s1.sort()
    return s1


def hologram(*data, transformation=1):
    if transformation == 1:
        return map(f1, data)
    elif transformation == 2:
        return map(f2, data)
    elif transformation == 3:
        return map(f3, data)
    elif transformation == 4:
        return map(f4, data)


data = ["You can restore",
        "any object",
        "using a hologram"]
print(*hologram(*data, transformation=4), sep='\n')