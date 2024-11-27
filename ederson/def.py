'''def ya():
    print("esctvgyh")
ya()

oi=input()
def d_dust2(nome):
    print('socorro',nome,'seu merda')
d_dust2(oi)

def inf(nomes):
    print("oi",nomes,"seu !!!!!!!!")
while True:
    nomes=input('nome: ')
    inf(nomes)

def cal_pag(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    print(salario)
cal_pag(35,20)

def soma(x,y):
    result=x+y
    return result
a=int(input("primeiro número: "))
b=int(input("segundo número: "))
res=soma(a,b)
print('Soma: ',res)

def inverte(nome,sobrenome):
    inverso=sobrenome+" , "+nome
    return inverso
nome=input("nome: ")
sobrenome=input("sobrenome: ")
invertido=inverte(nome,sobrenome)
print("Olá",invertido)

def par(x):
    if (x%2)==0:
        return True
    else:
        return False
while True:
    num=int(input("numero: "))
    if par(num):
        print("numero é par")
    else:
        print("numero é impar")

def cadastro():
    name=input("Qual seu nome: ")
    age=int(input("Idade: "))
    return name,age

print("Iniciando cadastro...")
nome,idade=cadastro()
print("Castro realizado com sucesso: ")
print("Seu nome é",nome,"e você tem",idade,"anos de idade")'''