x = str(input())
if x == 'круг':
    def func_krug():
        pi = 3.14
        r = int(input())
        s = pi * r **2
        return s
    print(func_krug())
if x == 'треугольник':
    def func_treug():
        a = int(input())
        h = int(input())
        s = a * h / 2
        return s
    print(func_treug())
if x == 'прямоугольник':
    def func_pram():
        a = int(input())
        b = int(input())
        s = a * b
        return s 
    print(func_pram())