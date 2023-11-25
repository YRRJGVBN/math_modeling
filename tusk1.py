def func():
    a = int(input())
    b = []
    while a != 0:
        b.append(a)
        a = int(input())
    c = sum(b) / len(b)
    return c
print(func())