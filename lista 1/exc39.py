def media_harmonica(list):
    deno = 0
    size = len(list)
    for i in range(0, size):
        if(list[i]==0):
            print('sem divisao por zero')
        else:
            deno += (1/list[i])
    return size/deno
list = [1,2,4]
print(media_harmonica(list))