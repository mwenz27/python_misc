def x(i):
    x = i
    x = x * (x +1)
    return x

for i in range(10):
    print(i, x(i))
    