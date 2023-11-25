import numpy as np
a = int(input())
b = int(input())
N = int(input())
def funk_funk(a, b, N):
    c = np.linspace(a, b, N)
    x = []
    for i in c:
        d = i ** 2
        x.append(d)
    return x
print(funk_funk(a + 1, b - 1, N))