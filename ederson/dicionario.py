'''translate={}
translate['chan eil']='no'
translate['tha']='yes'
translate['ghrian']='sun'

print(type(translate))
print(translate)
print(translate["ghrian"])

translate={'oi':'AAAAAAA','hit':'shit'}
print(translate)
del (translate['hit'])

#                   item / noitem mensagem
print(translate.pop('hit','kys'))

translate.clear()
print(translate)
print('hit' in translate)

a={'apple':'fruit','car':'shoe','men':'a'}
print('fruit' in a.values())
print(a.values())

a={'apple':'fruit','car':'shoe','men':'a'}
print(a)
a ['apple']='maçã'
print(a)'''

dados = {
    'CrossFox':{'km':35000,'ano':2005},
    'DS5':{'km':17000,'ano':2015},
    'Fusca':{'km':130000,'ano':1979},
    'Jetta':{'km':56000,'ano':2011},
    'Passat':{'km':62000,'ano':1999}
}

print(dados)
print(dados.get('gol','veículo não encontrado'))