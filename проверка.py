V = 60
N = 0.5

V0 = V / 3.6
Stotal = (V0 ** 2) / (2 * N * 9.8)
a = -(V0 ** 2) / (2 * Stotal)
t = -V0 / a
print(Stotal)
print(V0)
print(a)