class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    def desconto(self,desconto):
        return self.preco-(self.preco*(desconto/100))