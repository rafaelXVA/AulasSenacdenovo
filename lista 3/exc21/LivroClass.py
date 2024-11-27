class Livro:
    def __init__(self,estoque,titulo):
        self.estoque=estoque
        self.titulo=titulo
    def tirar(self):
        return self.estoque-1
    def colocar(self):
        self.estoque+1
    def mostrar(self):
        print(self.estoque,'\n',self.titulo)