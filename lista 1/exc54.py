def media(dic):
    notas = sum(dic.values())  
    qnt = len(dic)     
    if qnt == 0:              
        return 0
    media = notas / qnt  
    return media
notas = {
    "pedro": 8.5,
    "ryan": 7.0,
    "rafael": 9.0,
    "tiago": 6.5
}
print(media(notas))  