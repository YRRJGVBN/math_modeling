import math
import numpy as np
a = float(input())
n = int(input())
b = np.zeros((1,n))
def func_stepen(a, b):
    for i in b:
        i += a
    return b
print(math.prod(func_stepen(a, b)))