"""
//substituir um item da lista//
list=["banana"]
list[0]="oi"
print(list)

list=["a","b","c","d","f","g","h"]
list[0:2]=["america","ya"]
print(list)

//remover//
list=["a","b","c","d","e","f","g","h","i","j"]
print(len(list))
list[0:4]=[]
print(list)
print(len(list))

//outro remover

list=["a",'b','c','d','e','f']
del list[1]
print(list)
del list[0:4]
print(list)

//adicionar//
list=["a","b","d","f"]
print(list)
list[2:2]="c"
print(list)
list[4:4]="e"
print(list)

//outro adicionar//

list=[1,2,3,4,5,6,7,8,9]
list.insert(11,10)
print(list)

//adicionar ao final//

list=[1,2,3,4,5,6,7]
list.append(10)
print(list)

//organizar em ordem crescente e inverter//

list=[1,5,4,2,8,7]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

//verificar onde o item está na lista e se tem o item//

list=[1,2,3,4,5,6,7,9]
print(list.index(7))
print(6 in list)

//contar quantas vezes um item aparece na lista//

list=[55,564,564,126668,54561,18,2551,1564,256654,2,2515,5164,561,15,564,546405,354,848,156,132,4051,12312,126]
print(list)
print(list.count(564)

list=[1,2,3,4,5,6,7,8,9]
print(list)
list.pop()
print(list)
list.pop(0)
print(list)"""

list=[1,2,3]
list.extend([4,5])
print(list)