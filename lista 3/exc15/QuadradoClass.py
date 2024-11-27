class Quadrado:
    def __init__(self,largura,comprimento):
        self.largura=largura
        self.comprimento=comprimento
    def area(self):
        print(self.largura*self.comprimento)
    def perimetro(self):
        print(self.largura+self.comprimento)