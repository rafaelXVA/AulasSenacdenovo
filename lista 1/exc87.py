def p(n):
    for i in range(0, n + 1, 2):  
        yield i
for x in p(10):
    print(x)