m = int(input())
h = int(input())
v = int(input())
g = 9.8
def func_E(m, h, v, g):
    ep = m * g * h
    ek = m * v ** 2 / 2
    em = ep + ek
    return em
print(func_E(m, h, v, g))