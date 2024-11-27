class Relogio:
    def __init__(self,hora,minuto):
        self.hora=hora
        self.minuto=minuto
    def mostar(self):
        print(f'{self.hora}:{self.minuto}')