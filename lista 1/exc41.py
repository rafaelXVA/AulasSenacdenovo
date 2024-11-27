def mediana(list):
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if(list[i]> list[j]):
                memory = list[j]
                list[j] = list[i]
                list[i] = memory
    size = len(list)
    medialist = round(size/2)-1
    media = (list[medialist]+list[medialist+1])/2
    return media
list = [10,9,8,7,6,5,4,3,2,1]
print(mediana(list))