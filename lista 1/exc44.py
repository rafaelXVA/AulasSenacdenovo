def prod(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + prod(a, b - 1)
    else:
        return -prod(a, -b)
print(prod(13, 5))  