def cont(n):
    for i in range(0, n + 1):
        yield i
for x in cont(5):
    print(x)