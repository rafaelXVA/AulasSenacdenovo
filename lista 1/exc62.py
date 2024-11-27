def bubblesort(list):
    n = len(list)
    for i in range(n):
        change = False
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                change = True
        if not change:
            break
    return list
list = [23,23,235,21,67,31,20]
print(bubblesort(list)) 