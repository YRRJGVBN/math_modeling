import math
V= float(input())
N = float(input())
V0 = V / 3.6
Stotal = (V0 ** 2) / (2 * N * 9.8)
a = -(V0 ** 2) / (2 * Stotal)
t = -V0 / a
print(t)
print(a)
print(math.ceil(Stotal))
