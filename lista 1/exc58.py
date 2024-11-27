def cont(x):
    count = 0
    for char in x:
        if char.isupper():
            count += 1
    return count
x = "america Ya america"
print(cont(x))  