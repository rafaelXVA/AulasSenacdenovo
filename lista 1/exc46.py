def invert(list):
    if not list:
        return ''
    a, *b = list[::-1]
    return a + invert(b[::-1])

    

print(invert('americaYa'))  