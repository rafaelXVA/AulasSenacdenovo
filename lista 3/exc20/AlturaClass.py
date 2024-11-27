class Altura:
    def __init__(self,altura):
        self.altura=altura
    def verify(self):
        if self.altura>1.75:
            print('maior que 1,75')
        else:
            print('menor que 1,75')