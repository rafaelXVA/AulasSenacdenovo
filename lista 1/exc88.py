def square(n):
    for i in range(1, n + 1):  
        yield i ** 2  
for x in square(5):
    print(x)