class Vendedor():
    def __init__(self,nome,vendas):
        self.nome=nome
        self.vendas=vendas
    

vendedor1=Vendedor('ederson',1000)
print(vendedor1.nome)

vendedor2=Vendedor('rafael',1000)
print(vendedor2.vendas)