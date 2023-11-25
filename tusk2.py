def func_gen():
    b = []
    a = -1
    while a != 1:
        a = int(input())
        b.append(a)
    return b
b = func_gen()
x = 1
for i in b:
    x *= i
print(x)