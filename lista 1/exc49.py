def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mcdList(list):
    if len(list) == 1:
        return list[0]
    return mcd(list[0], mcdList(list[1:]))
x = [69, 40]
print(mcdList(x))  