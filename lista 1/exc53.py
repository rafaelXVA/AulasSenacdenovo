def cont(s):
    times = {}
    for char in s:
        if char in times:
            times[char] += 1
        else:
            times[char] = 1
    return times
s = "maestria7"
print(cont(s)) 