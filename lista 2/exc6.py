def diference(list1,list2):
    x=set(list1)
    y=set(list2)
    return list(x-y)
list1 = [10,20, 30, 40]
list2 = [20, 40, 60]
res=diference(list1,list2)
print(res)
