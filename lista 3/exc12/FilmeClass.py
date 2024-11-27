class Filme:
    def __init__(self,titulo,duracao):
        self.titulo=titulo
        self.duracao=duracao
    def exibir(self):
        print(f'titulo {self.titulo}')
        print(f'duração de {self.duracao} minutos')